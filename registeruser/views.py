from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from registeruser.forms import RegisterUserForm
from registeruser.models import RegisterUser

# Create your views here.

# The RegisterUserView class inherits from the CreateView class, and it uses the RegisterUser model,
# the registerUser.html template, and the RegisterUserForm form
class RegisterUserView(CreateView):
    model = RegisterUser
    template_name = 'template/registerUser.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('user:listUser')

# The ListUserRegisterView class inherits from the ListView class, and it's model is the RegisterUser
# model
class ListUserRegisterView(ListView):
    model = RegisterUser
    template_name = 'template/listUser.html'



