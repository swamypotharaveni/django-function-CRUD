from django.shortcuts import render, redirect
from myapp.forms import shopform
from myapp.models import shop1
from myapp import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,DetailView
from django.urls import reverse_lazy

def index(request):
    form =forms.shopform()
    if request.method == 'POST':
        form =forms.shopform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/list')
    return render(request, 'index.html', {'form': form})


def list(request):
    Shop1 = shop1.objects.all()
    return render(request, 'list.html', {'Shop1': Shop1})


def destroy(request,id):
    shop12 = shop1.objects.get(id=id)
    shop12.delete()
    return redirect('/list')


def edit(request,id):
    shop12=shop1.objects.get(id=id)
    return render(request,'edit.html', {'Shop12':shop12})

def update(request,id):
    shop12=shop1.objects.get(id=id)
    form=forms.shopform(request.POST,instance=shop12)
    if form.is_valid():
         form.save(commit=True)
         return redirect('/list')
    return render(request,'edit.html',{'Shop12': shop12})
class signup(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
class details(DetailView):
    model = shop1
    template_name = 'details.html'

