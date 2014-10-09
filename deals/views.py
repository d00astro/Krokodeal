from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from deals.models import Deal


class IndexView(generic.ListView):
    template_name = 'deals/deal_list.html'
    context_object_name = 'deals'
    
    def get_queryset(self):
        return Deal.objects.all()

def vote(request, deal_id):
    
    aDeal = get_object_or_404(Deal, pk=deal_id)
    
    if deal_id + "_up" in request.POST:
        aDeal.temperature += 1
    if deal_id + "_down" in request.POST:
        aDeal.temperature -= 1
    
    aDeal.save()
    return HttpResponseRedirect(reverse('deals:index'))