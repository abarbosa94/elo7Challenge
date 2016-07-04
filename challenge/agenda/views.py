from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from agenda.models import Contact
from agenda.forms import ContactForm
from agenda.functions.methods import Methods
from django.db.models import Q
from agenda.functions.twitterapi import Twitter

# Create your views here.



def home(request):
    return render(request,'index.html')

def statistics(request):
    contacts = Contact.objects.all()
    emails = contacts.values_list('email', flat=True)
    names = contacts.values_list('name', flat=True)
    methods = Methods()
    lowest_full_name = methods.calculate_lower_size(names)
    highest_full_name = methods.calculate_highest_size(names)
    avg_full_name = methods.calculate_size_avg(names)
    quartiles_full_name = methods.calculate_quartiles(names)
    names = methods.pick_first_names(names)
    lowest_first_name = methods.calculate_lower_size(names)
    highest_first_name = methods.calculate_highest_size(names)
    avg_first_name = methods.calculate_size_avg(names)
    quartiles_first_name = methods.calculate_quartiles(names)
    lowest_email = methods.calculate_lower_size(emails)
    highest_email = methods.calculate_highest_size(emails)
    avg_email = methods.calculate_size_avg(emails)
    quartiles_email = methods.calculate_quartiles(emails)


    return render(request,'statistics.html', {'list_size': len(contacts),
        'full_name': [lowest_full_name, highest_full_name, avg_full_name],
        'first_name': [lowest_first_name, highest_first_name, avg_first_name],
        'email': [lowest_email, highest_email, avg_email],
        'quartiles_full_name': quartiles_full_name, 
        'quartiles_first_name': quartiles_first_name, 
        'quartiles_email': quartiles_email})

class Create(CreateView):
    template_name = 'signin.html'
    model = Contact
    fields = ('name', 'email','twitter_user')
    success_url = reverse_lazy('list')

class Update(UpdateView):
    template_name = 'update.html'
    model = Contact
    fields = ('name', 'email', 'twitter_user')
    success_url = reverse_lazy('list')
   

class Delete(DeleteView):
    model = Contact
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('list')


class List(ListView):
    template_name = 'list.html'
    model = Contact
    context_object = 'name'
    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs) 
        tweet = Twitter()
        contacts = Contact.objects.all()
        users = contacts.values_list('twitter_user', flat=True)
        contacts = tweet.get_last_tweet(users, contacts)
        return context

class SearchList(ListView):
    template_name = 'results.html'
    model = Contact
    def get_queryset(self):
        result = super(SearchList, self).get_queryset()
        query = self.request.GET.get('query')
        if (query != ''):
            object_list = self.model.objects.filter(Q(name__icontains=query) | Q(email__icontains = query))

        else:
            object_list = self.model.objects.all()
        return object_list



   

