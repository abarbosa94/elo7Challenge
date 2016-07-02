from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

from agenda.models import Contact
from agenda.forms import ContactForm

def home(request):
        return render(request,'index.html')

class Create(CreateView):
        template_name = 'signin.html'
        model = Contact
        fields = ('name', 'email')
        success_url = reverse_lazy('list')

class List(ListView):
        template_name = 'list.html'
        model = Contact
        context_object = 'name'


