from django import relative_url_template

register = template.Library()

# This funciton cuts out all values of "arg" from the string
@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')

#register.filter('cut', cut)
