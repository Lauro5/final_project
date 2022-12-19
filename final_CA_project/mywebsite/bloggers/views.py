from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import SignupForm, LoginUserForm, PasswordChangingForm, EditUserProfileForm
from django.contrib.auth import authenticate, login, logout
from myapp.models import Blog, Blogcomment
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# def signUp(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your account is created succesfully!")
#             new_user = authenticate(
#                 username = form.cleaned_data['username'],
#                 password = form.cleaned_data['password1'],
#             )

#             login(request, new_user)
#             return redirect('home')
#         else:
#             messages.error(request, "Error")
#     else:
#         form = SignupForm()    
#     return render(request, "bloggers/register.html", {'form': form})

class SignUp(SuccessMessageMixin, generic.CreateView):
    form_class = SignupForm
    template_name = "bloggers/register.html"
    success_url = reverse_lazy('login')
    success_message = "User has been created, please login with your username and password"

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please submit the form carefully")
        return redirect('home')


class logIn(generic.View):
    form_class = LoginUserForm
    template_name = "bloggers/login.html"

    def get(self, request):
        form = self.form_class 
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        if request.method == "POST":
            form = LoginUserForm(request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username = username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, f"You have succesfully logged in as {username}")
                    return redirect('home')
                else:
                    messages.error(request, "Error")
            else:
                messages.error(request, "Username or password is invalid!")
        form = LoginUserForm()
        return render(request, "bloggers/login.html", {"form": form})


class logOut(LoginRequiredMixin, generic.View):
    login_url = 'login'
    def get(self, request):
        logout(request)
        messages.success(request, "User logged out")
        return redirect('home')


class profile(LoginRequiredMixin, generic.View):
    model = Blog
    login_url = 'login'
    template_name = "bloggers/profile.html"

    def get(self, request, user_name):
        user_related_data = Blog.objects.filter(author__username = user_name)
        context = {
            "user_related_data": user_related_data
        }
        return render(request, self.template_name, context)

class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    login_url = 'login'
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, "bloggers/password_change_success.html")

class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    login_url = 'login'
    form_class = EditUserProfileForm
    template_name = "bloggers/edit_user_profile.html"
    success_url = reverse_lazy('home')
    success_message = "User has been updated"

    def get_object(self):
        return self.request.user
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please submit the form carefully")
        return redirect('home')

class DeleteUser(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = User
    login_url = 'login'
    template_name = 'bloggers/delete_user_confirm.html'
    succes_message = "User has been deleted"
    success_url = reverse_lazy('home')