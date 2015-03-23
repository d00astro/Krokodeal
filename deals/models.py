from django import forms
from django.db import models
from django.forms import ModelForm
from django.utils.text import slugify
from deals import library
from django.conf import settings

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile

import base64
import hashlib
import hmac
import json
import time
 
TEMPERATURE_INCREASE = 7

class Deal(models.Model):

    #Mandatory fields
    title_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length=60, blank=True)
    link_url = models.URLField()

    price_decimal = models.DecimalField(max_digits=10, decimal_places=2)
    description_text = models.TextField() #Not sure if we should call it something else like _textarea this is the recommended type for long texts: https://docs.djangoproject.com/en/1.7/ref/models/fields/#textfield
    imageUrl_url = models.URLField(blank=True, null=True) #only for historical reasons and temporary placeholder of images
    thumbnail_image =  models.ImageField(upload_to="deal_thumbnails", blank=True, null=True, height_field='thumbnail_image_height', width_field='thumbnail_image_width')
    thumbnail_image_width = models.PositiveIntegerField(blank=True, null=True)
    thumbnail_image_height = models.PositiveIntegerField(blank=True, null=True)
    
    #Optional fields from here I'll add the blank=True
    vendor_text = models.CharField(max_length=100, blank=True, null=True)
    normalPrice_decimal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shippingCost_decimal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discountCode_text = models.CharField(max_length=200, blank=True)
    
    #Service fields
    dateAdded = models.DateTimeField(auto_now_add=True)
    expired = models.BooleanField(default=False)
    temperature = models.IntegerField(default=0)
    
    
    def save(self, *args, **kwargs):
        if not self.id:
            #Only set the slug when the object is created.
            self.slug = slugify(self.title_text[:56] + str(time.time())[-4:]) #Or whatever you want the slug to use
            
            #We only need to resize if we are saving directly
            if self.thumbnail_image:
                output = library.createThumbnailFromUpload(self.thumbnail_image.read())
                self.thumbnail_image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.slug, 'image/jpeg', len(output.getvalue()), None)
             
        super(Deal, self).save(*args, **kwargs)
        
    
    def __str__(self):              # __unicode__ on Python 2
        return self.title_text
    
    def canUpvote(self, aUserId):
        aProfile = Profile.objects.get(user=aUserId)
                
        if (aProfile in self.profilesThatUpvoted.all()):
            return False
        else:
            return True
        
        
    def canDownvote(self, aUserId):
        aProfile = Profile.objects.get(user=aUserId)
                
        if (aProfile in self.profilesThatDownvoted.all()):
            return False
        else:
            return True
        
    def upvote(self, aUserId):
        aProfile = Profile.objects.get(user=aUserId)

        
        if (aProfile in self.profilesThatUpvoted.all()):
            
            return False
        else:
            #He did not upvote before, let's check if he downvoted before
            if (aProfile in self.profilesThatDownvoted.all()):
                #we remove the downvote
                self.profilesThatDownvoted.remove(aProfile)
            else:
                self.profilesThatUpvoted.add(aProfile)
            
            self.temperature = self.temperature + TEMPERATURE_INCREASE
            return True

    def downvote(self, aUserId):
        aProfile = Profile.objects.get(user=aUserId)
        
        if (aProfile in self.profilesThatDownvoted.all()):
            print("already downvoted")
            
            return False
        else:
            #He did not upvote before, let's check if he upvoted before
            if (aProfile in self.profilesThatUpvoted.all()):
                #we remove the downvote
                self.profilesThatUpvoted.remove(aProfile)
            else:
                self.profilesThatDownvoted.add(aProfile)
            
            self.temperature = self.temperature - TEMPERATURE_INCREASE
            return True

# Create the form class.
class DealForm(ModelForm):
    class Meta:
        model = Deal
        fields = ['title_text', 'link_url','price_decimal', 'description_text', 'imageUrl_url','thumbnail_image']
        
        widgets={
            "title_text":forms.TextInput(attrs={'placeholder':'Claro y conciso: Que es?','class':'form-control'}),
            "description_text":forms.Textarea(attrs={'placeholder':'Curratelo un poco, convencenos de que acabas de encontrar un buen chollo!','class':'form-control'}),
            "link_url":forms.TextInput(attrs={'placeholder':'No te olvides del http://','class':'form-control'}),
            "price_decimal":forms.TextInput(attrs={'placeholder':'asi: 50.3','class':'form-control','type':'text'}),
            "imageUrl_url":forms.TextInput(attrs={'placeholder':'http://... Si no sabes, te pondremos unos gatos','class':'form-control'}),
        }
    
    def clean_imageUrl_url(self):
        url = self.cleaned_data['imageUrl_url'].lower()
        if(url):
            domain, path = library.split_url(url)
            #if not library.valid_url_extension(url) or not library.valid_url_mimetype(url):
            #    raise forms.ValidationError("Not a valid Image. The URL must have an image extensions (.jpg/.jpeg/.png)")
            return url    


#######
## Profile 
######
class Profile(models.Model):
    user = models.ForeignKey(User)
    upvotes = models.ManyToManyField(Deal, blank=True, related_name='profilesThatUpvoted')
    downvotes = models.ManyToManyField(Deal, blank=True, related_name='profilesThatDownvoted')
        
    def __str__(self):              # __unicode__ on Python 2
        return self.user.username
        
    def get_disqus_sso(self):
        
        # create a JSON packet of our data attributes
        data = json.dumps({
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
        })
        print(data)
        # encode the data to base64
        message = base64.b64encode(data.encode('UTF-8'))
        #message = base64.b64encode(bytes(data, 'UTF-8'))
        # generate a timestamp for signing the message
        timestamp = int(time.time())
        # generate our hmac signature
        messageAndTimestamp = '%s %s' % (message, timestamp)
        sig = hmac.HMAC(settings.DISQUS_SECRET_KEY.encode(), messageAndTimestamp.encode(), hashlib.sha1).hexdigest()
     
    # return a script tag to insert the sso message
        return """<script type="text/javascript">
        var disqus_config = function() {
            this.page.remote_auth_s3 = "%(message)s %(sig)s %(timestamp)s";
            this.page.api_key = "%(pub_key)s";
        }
        </script>""" % dict(
            message=message,
            timestamp=timestamp,
            sig=sig,
            pub_key=settings.DISQUS_PUBLIC_KEY,
        )


########
### Extending User Creation Form
#######

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            
            #He de crear el profile just despres
            myNewProfile = Profile()
            myNewProfile.user = user
            myNewProfile.save()
        return user
    