from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from .models import Event, Comments, LinkEvent
from .forms import CommentForm


class EvenNews(FormMixin, DetailView):
    model = Event
    template_name = 'event/event.html'
    context_object_name = 'event_news'
    form_class = CommentForm
    # success_url = '/'
    bad_words = ['плохое', 'зачем', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        comments = Comments.objects.filter(event=event).order_by('-create_data')
        links = LinkEvent.objects.filter(event=event)
        context['comments'] = comments
        context['links'] = links
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.event = self.get_object()
        self.object.author = self.request.user

        comment_text = form.cleaned_data.get('text', '').lower()
        if any(bad_word in comment_text for bad_word in self.bad_words):
            form.add_error(None, 'Комментарий содержит запрещенные слова')
            return self.form_invalid(form)

        self.object.save()
        return HttpResponseRedirect(self.request.path)

    def form_invalid(self, form):
        event = self.get_object()
        comments = Comments.objects.filter(event=event).order_by('-create_data')
        links = LinkEvent.objects.filter(event=event)
        context = self.get_context_data(comments=comments, links=links, form=form)
        return self.render_to_response(context)

def event_list(request):
    events = Event.objects.all().order_by('-date_event')
    years = list(events.dates('date_event', 'year'))[::-1]
    events_by_year = {}
    for year in years:
        events_by_year[year.year] = events.filter(date_event__year=year.year)
    context = {'events_by_year': events_by_year}
    return render(request, 'event/archive.html', context)
