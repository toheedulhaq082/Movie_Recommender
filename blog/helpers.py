from django.utils.text import slugify
import random
import string

def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
    return res

def generate_slug(text):
    from .models import BlogModel
    new_slug = slugify(text)
    return new_slug 