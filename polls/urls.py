from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_form, name='question_form'),
    # Добавьте другие URL-шаблоны по мере необходимости
]