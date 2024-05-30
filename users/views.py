from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from properties.models import Property
from users.forms import RegisterForm
# Create your views here.


def first_view(request):
    properties = Property.objects.all()
    context = {
        "properties": properties
    }
    print('firts ',properties)
    return render(request, "properties.html", context=context)

class UserRegister(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:success')
    
    def form_valid(self, form):
        form.save()
        return super(UserRegister, self).form_valid(form)
        
