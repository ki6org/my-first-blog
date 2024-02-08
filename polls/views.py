from django.shortcuts import render
from .models import Question

def question_form(request):
    return render(request, 'question_form.html')


# Create your views here.
