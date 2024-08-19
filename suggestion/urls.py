from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog.models import BlogModel
from .views import HomePageView

urlpatterns = [
    # path('', views.suggestion, name='home'),
    path('', HomePageView.as_view(), name='home'),
    path('random/', views.random, name='random'),
    path('similar/', views.similar, name='similar'),
    path('mood/', views.mood, name='mood'),
]

if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns() 