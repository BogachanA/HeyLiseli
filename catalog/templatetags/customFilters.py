from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='substring',is_safe=True)
@stringfilter
def substring(value,arguments):
    args=arguments.split(",")
    start=int(args[0])
    end=int(args[1])
    return value[start:end]

@register.filter(name='len',is_safe=True)
def getLength(value):
    return len(value)
