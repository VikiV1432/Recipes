from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView, View
from .forms import SignUpForm, EditProfileForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages 
from django.shortcuts import get_object_or_404
# Create your views here.

class SignInPage(TemplateView):
    template_name="accounts/sign-in.html"
    def get(self, request, *args, **kwargs):
        return self.render_to_response(context=self.get_context_data())
    def post(self, request, *args, **kwargs):
        sign_in_method=request.POST.get('sign-in-method')
        password=request.POST.get("password")
        try:
            user=User.objects.get(email=sign_in_method)
            username=user.username
        except:
            username=sign_in_method
        user=authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,"Wrong Credentials!")
        return self.render_to_response(context=self.get_context_data())
    
class SignUpPage(CreateView):
    model=User
    form_class=SignUpForm
    template_name='accounts/sign-up.html'
    success_url=reverse_lazy("sign-in")


class ProfilePage(View):
    def get(self, request, username, *args, **kwargs):
            user=get_object_or_404(User,username=username)
            return render(request, "accounts/profile.html", {"user":user})
    def post(self, request, username, *args, **kwargs):
        pass


class EditProfilePage(View):
    def get(self, request, *args, **kwargs):
            user=request.user
            form=EditProfileForm(instance=user.profile)
            return render(request, "accounts/edit-profile.html", {'form':form})
    def post(self, request, *args, **kwargs):
        user=request.user
        form=EditProfileForm(data=request.POST,files=request.FILES, instance=user.profile)
        if form.is_valid():
             form.save()
             return redirect(reverse('profile',kwargs={'username':user.username}))
        else:
             return render(request, "accounts/edit-profile.html", {'form':form})

