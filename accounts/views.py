from django.shortcuts import render, redirect
from . import views
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('lijiang_guide:index')
        
    return render(request, 'registration/register.html', {
        'form': form,
    })