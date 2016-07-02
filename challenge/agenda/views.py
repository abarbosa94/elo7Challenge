from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from agenda.models import Contact
from agenda.forms import ContactForm
from agenda.methods import Methods
from django.db.models import Q

# Create your views here.



def home(request):
    return render(request,'index.html')

def statistics(request):
    contacts = Contact.objects.all()
    methods = Methods()
    lowest_size = methods.calculate_lower_full_name_size(contacts)
    highest_size = methods.calculate_highest_full_name_size(contacts)

    return render(request,'statistics.html', {'list_size': len(contacts), 'minimum_full_name': lowest_size, 'maximum_full_name': highest_size})

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



   

