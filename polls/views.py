from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from polls.models import Question, Choice
from .forms import ContactForm
from django.contrib.auth.decorators import login_required


@login_required #user to ensure user is logged in


# Create your views here.



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Perform actions (e.g., send email)
            return redirect('polls:thanks')
    else:
        form = ContactForm()
    return render(request, 'polls/contact.html', {'form': form})


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')
    paginator = Paginator(latest_question_list ,5)  #show 5 question per page
    page_number=paginator.get_page('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'polls/index.html',{"page_obj":page_obj})

#class base approach
from  django.views import View
from django.http import HttpResponse

# class indexview(View)
def get(self, request):
    return HttpResponse("hello world you are at the poll index")

def detail(request, question_id):
    # view to display a specific questuion
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    # view to display the result of a specigic question
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question} )

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice._set_get(pk = request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render (request, 'polls/details.html',{
            'question': question,
            'error_message': "you didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls.results', args=(question.id)))

