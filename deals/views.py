from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout


from deals.models import Deal, DealForm


class IndexView(generic.ListView):
    template_name = 'deals/deal_list.html'
    context_object_name = 'deals'
    
    def get_queryset(self):
        return Deal.objects.all()
    
# Create the form class.
@login_required
def addDeal(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DealForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # Create a form instance from POST data.
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/deals/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DealForm()
        
    return render(request,'deals/deal_add.html', {'form': form,})
    
def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/deals/')

@login_required
def vote(request, deal_id):
    
    aDeal = get_object_or_404(Deal, pk=deal_id)
    
    if deal_id + "_up" in request.POST:
        aDeal.temperature += 1
    if deal_id + "_down" in request.POST:
        aDeal.temperature -= 1
    
    aDeal.save()
    return HttpResponseRedirect(reverse('deals:index'))