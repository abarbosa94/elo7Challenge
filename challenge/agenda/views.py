from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from agenda.models import Contact
from agenda.forms import ContactForm
from django.db.models import Q

# Create your views here.



def home(request):
    return render(request,'index.html')

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
        #print self.model.objects.all()
        result = super(SearchList, self).get_queryset()
        query = self.request.GET.get('query')
        if (query != ''):
            object_list = self.model.objects.filter(Q(name__icontains=query) | Q(email__icontains = query))

        else:
            object_list = self.model.objects.all()
        return object_list


