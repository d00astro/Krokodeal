from django.shortcuts import render

from deals.models import Deal


def index(request):
    deals = Deal.objects.all()
    context = {'deals': deals}
    return render(request, 'deals/index.html', context)