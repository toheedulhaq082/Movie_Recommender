from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class ActorSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return ['nicolas_cage']

    def location(self, item):
        return reverse(item)