from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from deals.models import Deal

class HotDealsFeed(Feed):
    title = "La lista de chollos"
    link = "/chollos_feed/"
    description = "Lista con los ultimos Chollos de Chollometro"

    def items(self):
        return Deal.objects.order_by('-dateAdded')[:10]

    def item_title(self, item):
        return item.title_text

    def item_description(self, item):
        return item.description_text

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('deals:dealDetail', args=[item.slug])