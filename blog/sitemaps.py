from django.contrib.sitemaps import Sitemap
from .models import BlogModel

class BlogSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return BlogModel.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
