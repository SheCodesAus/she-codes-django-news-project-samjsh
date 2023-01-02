from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import get_object_or_404
#from django.contrib.auth import get_user_model


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class CreateAuthorView(generic.DetailView): #samtest123
    model = CustomUser
    template_name = 'news/author.html'
    context_object_name = 'author'
    
    def get_object(self, queryset:None): 
        return get_object_or_404(CustomUser,
        username=self.kwargs['author_username'])
        # calls customuser.object.get username based on username and if it can't find it will return a 404 error.
