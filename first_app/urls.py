
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('delete/<int:roll>', views.delete_student, name='delete_student'),
    path('forms/', views.django_form),
    path('django_forms/', views.show_all, name='django_forms'),
]
