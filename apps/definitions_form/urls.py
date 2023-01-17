from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateForm.as_view()),
    path('get_form/', views.GetForm.as_view())
]