from django.shortcuts import render, redirect
from .forms import QuestionForm

def question_form(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_form')
    else:
        form = QuestionForm()
    return render(request, 'question_form.html', {'form': form})