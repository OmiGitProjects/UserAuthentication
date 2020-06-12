from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):

        if request.method == 'POST':
                form = UserRegisterForm(request.POST)
                if form.is_valid():
                        form.save()
                        username = form.cleaned_data.get('username')
                        messages.success(request, f"Your Account has been Created {username}, Now You can Login your Account!")
                        return redirect('Login')
        else:
                form = UserRegisterForm()
        return render(request, 'userApp/register.html', {'form':form,'title':'user register'})