from django.shortcuts import render, redirect
from . import models
# from 'first_app/forms' import djangoForm
from . forms import djangoForm
# Create your views here.


def home(request):
    students = models.Students.objects.all()
    return render(request, 'index.html', {'data': students})


def delete_student(request, roll):
    models.Students.objects.get(pk=roll).delete()
    return redirect('homepage')


def django_form(request):
    form = djangoForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'forms.html', {'form': form})


def show_all(request):
    allData = models.modelPractice.objects.all()
    return render(request, 'django_models.py', {'data': allData})
