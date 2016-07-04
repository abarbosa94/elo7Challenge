from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from agenda.models import Contact
from agenda.forms import ContactForm
from agenda.functions.methods import Methods
from django.db.models import Q
from agenda.functions.twitter import Test

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
    names = methods.pick_first_names(names)
    lowest_first_name = methods.calculate_lower_size(names)
    highest_first_name = methods.calculate_highest_size(names)
    avg_first_name = methods.calculate_size_avg(names)
    lowest_email = methods.calculate_lower_size(emails)
    highest_email = methods.calculate_highest_size(emails)
    avg_email = methods.calculate_size_avg(emails)

    return render(request,'statistics.html', {'list_size': len(contacts),
        'minimum_full_name': lowest_full_name, 'maximum_full_name': highest_full_name, 'avg_full_name': avg_full_name,
        'minimum_first_name': lowest_first_name, 'maximum_first_name': highest_first_name, 'avg_first_name': avg_first_name,
        'minimum_email': lowest_email, 'maximum_email': highest_email, 'avg_email': avg_email})

class Create(CreateView):
    template_name = 'signin.html'
    model = Contact
    fields = ('name', 'email')
    success_url = reverse_lazy('list')

class Update(UpdateView):
    template_name = 'update.html'
    model = Contact
    fields = ('name', 'email')
    success_url = reverse_lazy('list')
   

class Delete(DeleteView):
    model = Contact
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('list')


class List(ListView):
    template_name = 'list.html'
    model = Contact
    context_object = 'name'
    contacts = Contact.objects.all()
    emails = contacts.values_list('email', flat=True)
    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)
        test = Test()
        tweet = test.get_last_tweet('bbcbrasil')
        context['tweet'] = tweet
        print 'hi'
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



   

