from django import forms
from django.db import models
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

TEMPERATURE_INCREASE = 7

class Deal(models.Model):

    #Mandatory fields
    title_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length=60, blank=True)
    link_url = models.URLField()

    price_decimal = models.DecimalField(max_digits=10, decimal_places=2)
    description_text = models.TextField() #Not sure if we should call it something else like _textarea this is the recommended type for long texts: https://docs.djangoproject.com/en/1.7/ref/models/fields/#textfield
    imageUrl_url = models.URLField(default="http://lorempixel.com/g/100/100/cats") #This should probably be an ImageField in the long term...
    
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
            self.slug = slugify(self.title_text) #Or whatever you want the slug to use
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
        fields = ['title_text', 'link_url','price_decimal', 'description_text', 'imageUrl_url']
        
        widgets={
            "title_text":forms.TextInput(attrs={'placeholder':'Claro y conciso: Que es?','class':'form-control'}),
            "description_text":forms.Textarea(attrs={'placeholder':'Curratelo un poco, convencenos de que acabas de encontrar un buen chollo!','class':'form-control'}),
            "link_url":forms.TextInput(attrs={'placeholder':'No te olvides del http://','class':'form-control'}),
            "price_decimal":forms.TextInput(attrs={'placeholder':'asi: 50,3','class':'form-control','type':'text'}),
            "imageUrl_url":forms.TextInput(attrs={'placeholder':'http://... Si no sabes, te pondremos unos gatos','class':'form-control'}),
        }
    
       
    
    def clean_imageUrl_url(self):
        print("Petupetu2")
        if(self.cleaned_data['imageUrl_url'] == ""):
            print("petupetu3")
            self.cleaned_data['imageUrl_url'] = "http://lorempixel.com/g/100/100/cats"
            
        return self.cleaned_data['imageUrl_url'] 


#######
## Profile 
######
class Profile(models.Model):
    user = models.ForeignKey(User)
    upvotes = models.ManyToManyField(Deal, blank=True, related_name='profilesThatUpvoted')
    downvotes = models.ManyToManyField(Deal, blank=True, related_name='profilesThatDownvoted')
        
    def __str__(self):              # __unicode__ on Python 2
        return self.user.username
    
    """ def __init__(self, aUser):
        user = aUser
        votes = 0
    
    def __init__(self, aUser, aVotes):
        user = aUser
        votes = aVotes"""
        


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