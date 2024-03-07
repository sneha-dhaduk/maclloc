from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# from tinymce.models import HTMLField
# from tinymce import models as tinymce_models

# Create your models here.
class macllocmedia(models.Model):
    image=models.ImageField(upload_to='images/')
    banner=models.ImageField(upload_to='images/')
    image1=models.ImageField(upload_to='images/')
    image2=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=100)
    contain=models.CharField(max_length=50)
    contain1=models.CharField(max_length=500)
    imagecontain=models.CharField(max_length=1000)
    months=models.IntegerField()
    paragraph=models.CharField(max_length=2000)
    
    def __str__(self):
        return self.contain
    
def validate_ten_digit(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError(_('enter a valid ten-digit number'))
class student(models.Model):
    name=models.CharField(max_length=15)
    mobile=models.CharField(max_length=10,validators=[validate_ten_digit])
    email=models.EmailField()
    message=models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class studentreview(models.Model):
    photo=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=100)
    review=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name