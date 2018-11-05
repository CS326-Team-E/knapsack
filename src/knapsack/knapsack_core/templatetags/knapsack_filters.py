from django import template

register = template.Library()

@register.filter
def modulo(a, b):
    return a % b
    
@register.filter
def has_substring(string1, string2):
    return string2.lower() in string1.lower()