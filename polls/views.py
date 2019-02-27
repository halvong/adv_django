from django.views import generic
from django.shortcuts import redirect
from django.views.generic.base import TemplateResponseMixin
from .models import Question, Choice
from .mixins import RequireLoginMixin

class IndexView(RequireLoginMixin, generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    print ("1a. IN IndexView")

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

#---
class DetailView(generic.DetailView):
    print ("1b. IN DetailView")
    model = Question
    template_name = 'polls/detail.html'

#---
class DeleteView(generic.DeleteView):
    print ("1c. IN DeleteView")
    model = Question
    success_url = "/polls/"

#---
class VoteView(generic.View):

    def get_queryset(self, choice_id):
        return Choice.objects.get(pk=choice_id)

    def post(self, request, pk):
        print ("2. IN VoteView POST")
        question_id = pk
        choice_id = request.POST.get('choice', None)
        try:
            queryset = self.get_queryset(choice_id)
            print ("query:",queryset.choice_text)
        except (KeyError, Choice.DoesNotExist):
            return redirect('polls:detail', pk=question_id)
        else:
            queryset.votes += 1
            queryset.save()
            return redirect('polls:vote_result', pk=question_id)

#---
class ResultsView(TemplateResponseMixin, generic.View):
    template_name = 'polls/results.html'

    def get_queryset(self, question_id):
        return Question.objects.get(pk=question_id)

    def get(self, request, pk):
        print ("4. IN ResultsView get")
        queryset = self.get_queryset(pk)
        context = {'question': queryset}
        return self.render_to_response(context)

#---
class SwitchboardView(generic.View):
    def get(self, request, pk):
        print ("3. IN SwitchboardView get")
        view = ResultsView.as_view()
        return view(request, pk)

    def post(self, request, pk):
        print ("1. IN SwitchboardView post")
        view = VoteView.as_view()
        return view(request, pk)
