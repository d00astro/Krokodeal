from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import authenticate, login, logout

from deals.models import Deal, DealForm, MyUserCreationForm


class newDealsView(generic.ListView):
    template_name = 'deals/deal_list.html'
    context_object_name = 'deals'
    
    def get_queryset(self):
        dealList = Deal.objects.all().order_by('-dateAdded')[0:10]
        dealPaginator = Paginator(dealList,2)
        
        #page = request.GET.get('page')
        page = self.kwargs.get('page')
        
        print(page)
        
        if(page == None):
            page = 1
            
        try:
            deals = dealPaginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            deals = dealPaginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            deals = dealPaginator.page(dealPaginator.num_pages)
        
        return deals
    
class hotDealsView(generic.ListView):
    template_name = 'deals/deal_list.html'
    context_object_name = 'deals'
    
    def get_queryset(self):
        return Deal.objects.filter(temperature__gte='100').order_by('-dateAdded')[0:10]
    
# Create the form class.
@login_required
def addDeal(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DealForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            print("post_check")
            # process the data in form.cleaned_data as required
            # Create a form instance from POST data.
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/deals/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DealForm()
        
    return render(request,'deals/deal_add.html', {'form': form,})

#Register user
def registerView(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyUserCreationForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # Create a form instance from POST data.
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/deals/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MyUserCreationForm()
        
    return render(request,'deals/register.html', {'form': form,})

def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/deals/')

@login_required
def vote(request, deal_id):
    
    aDeal = get_object_or_404(Deal, pk=deal_id)
    
    if deal_id + "_up" in request.POST:
        aDeal.upvote(request.user.id)
    if deal_id + "_down" in request.POST:
        aDeal.downvote(request.user.id)
    
    aDeal.save()
    return HttpResponseRedirect(reverse('deals:new'))


class disclaimer(generic.ListView):
    template_name = 'deals/disclaimer.html'
    
    def get_queryset(self):
        return None
    
class about(generic.ListView):
    template_name = 'deals/about.html'
    
    def get_queryset(self):
        return None
    
