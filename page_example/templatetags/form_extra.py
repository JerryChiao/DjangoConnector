from django import template


register = template.Library()

@register.filter(name='addcls')
def addcls(field, css):
   return field.as_widget(attrs={"class":css})


@register.filter(name='onchange')
def onchange(field, func):
   return field.as_widget(attrs={"onchange":func})

