def is_student(user):
    return hasattr(user, 'student')

def is_teacher(user):
    return hasattr(user, 'teacher')

from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
