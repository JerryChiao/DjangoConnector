from django import template


register = template.Library()

@register.filter(name='addcls')
def addcls(field, css):
   return field.as_widget(attrs={"class":css})

