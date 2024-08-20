from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return ['home', 'random', 'similar', 'mood']

    def location(self, item):
        return reverse(item)