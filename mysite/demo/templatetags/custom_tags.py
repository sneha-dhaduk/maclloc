from django import template
import os

register=template.Library()

@register.filter()
def image_exists(image_path):
    return os.path.isfile(image_path)