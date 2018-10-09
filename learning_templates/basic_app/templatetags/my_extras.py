from django import template

register = template.Library()

# line 6 alt to line 15 - decorator approach to register custom filter
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of 'arg' from the string!
    """

    return value.replace(arg,'')

# register.filter('cut',cut)
    #'cut' string you call it, cut is the method
