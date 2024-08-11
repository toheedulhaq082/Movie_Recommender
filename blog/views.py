from django.shortcuts import render
from .models import BlogModel

# Create your views here.
def blog(request):
    context = {'blogs': BlogModel.objects.all()}
    return render(request, 'blog.html', context=context)

def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context=context)