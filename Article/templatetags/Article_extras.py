from django import template

from ..models import Catagory

register = template.Library()

@register.inclusion_tag("shared/catagory_navbar.html")
def catagory_navbar():
    return {
        'Catagory':Catagory.objects.filter(status=True)
    }