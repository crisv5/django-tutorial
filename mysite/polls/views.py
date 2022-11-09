
from typing import Any, Optional


from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.query import QuerySet
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name: str = "polls/index.html"
    context_object_name: Optional[str] = "latest_question_list"

    def get_queryset(self) -> QuerySet[Any]:
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name: str = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name: str = "polls/results.html"


def holis(request):
    return HttpResponse("Holis.")


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        context = {"question": question, "error_message": "You didn't select a choice"}
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
