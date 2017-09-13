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

@register.filter(name='add_',is_safe=True)
def update_value(var,toAdd):
    var+=toAdd
    return var

@register.filter(name='_add',is_safe=True)
def update_value(var,toAdd):
    var=toAdd+var
    return var

@register.filter(name='tostr',is_safe=True)
def tostring(value):
    return str(value)

@register.filter(name='div',is_safe=True)
def divide(value,arg):
    arg=int(arg)
    return value/arg

