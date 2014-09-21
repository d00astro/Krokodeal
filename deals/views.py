from django.shortcuts import render
from django.views import generic

from deals.models import Deal


class IndexView(generic.ListView):
    template_name = 'deals/index.html'
    context_object_name = 'deals'
    
    def get_queryset(self):
        return Deal.objects.all()