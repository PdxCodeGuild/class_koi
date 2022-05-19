from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question
# from django.http import Http404
# from django.template import loader

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list,}
    return render(request, 'polls_app/index.html', context)
    
    # template = loader.get_template('polls_app/index.html')
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context,request))

def detail (request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls_app/detail.html', {'question': question})
    
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    # return render(request, 'polls_app/detail.html',{'question': question})
    
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls_app/results.html', {'question': question})
    
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls_app/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls_app:results', args=(question.id,)))
    
    # return HttpResponse("You're voting on question %s." % question_id)
