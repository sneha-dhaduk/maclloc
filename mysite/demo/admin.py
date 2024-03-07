from django.contrib import admin
from . import models
# Register your models here.
class MacllocAdmin(admin.ModelAdmin):
    list_display=['title','image','banner','image1','image2','contain','months','contain1','imagecontain','paragraph']
    list_filter=['title']
    search_fields=['contain__startswith']
    
admin.site.register(models.macllocmedia,MacllocAdmin)   

admin.site.register(models.student)

class ReviewAdmin(admin.ModelAdmin):
    list_display=['name','photo','review']
admin.site.register(models.studentreview,ReviewAdmin)