from django import template


register = template.Library()


def javascript_variables(context):
    """A template tag to insert the view and settings variables into the
    page so they can be used in javascript"""
    view_variables = context.get('vars', {})
    usr = context.get('usr', {})
    return {'vars': view_variables, 'usr': usr}

register.inclusion_tag('tags/jsvars.html',
                       takes_context=True)(javascript_variables)
