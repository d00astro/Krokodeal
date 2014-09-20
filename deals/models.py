from django.db import models

class Deal(models.Model):

    #Mandatory fields
    title_text = models.CharField(max_length=200)
    link_url = models.URLField()
    vendor_text = models.CharField(max_length=100)
    price_decimal = models.DecimalField(max_digits=10, decimal_places=2)
    description_text = models.TextField() #Not sure if we should call it something else like _textarea this is the recommended type for long texts: https://docs.djangoproject.com/en/1.7/ref/models/fields/#textfield
    imageUrl_url = models.URLField() #This should probably be an ImageField in the long term...
    
    #Optional fields from here I'll add the blank=True
    normalPrice_decimal = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    shippingCost_decimal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, )
    discountCode_text = models.CharField(max_length=200, blank=True)
    
    #Service fields
    dateAdded = models.DateTimeField(auto_now_add=True)
    expired = models.BooleanField(default=False)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.title_text