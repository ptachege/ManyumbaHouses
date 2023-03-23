from django import template
from HouseListing.models import *
register = template.Library()


@register.inclusion_tag('HouseListing/_categories.html')
def show_categories():
    all_categories = Type.objects.all()
    context = {
        'all_categories': all_categories
    }
    return context


@register.inclusion_tag('HouseListing/_cities.html')
def show_cities():
    all_cities = Cities.objects.all()
    context = {
        'all_cities': all_cities
    }
    return context
