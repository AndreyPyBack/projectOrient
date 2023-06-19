from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm, LoginUserForm, EventForm, LinkEventForm, TrainingForm
from .models import Castom
from event.models import Event

from event.models import LinkEvent

from training.models import Training

from event.models import Comments


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('main:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        custom = Castom.objects.create(
            user=self.object,
            date_of_birth=form.cleaned_data['date_of_birth'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )
        return response


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self):
        if self.request.user.groups.filter(name='Redactor').exists():
            return reverse_lazy('profile')

        return reverse_lazy('main:main')


def editor_profile(request):
    return render(request, 'users/redactor.html')


class LinkEventEditor:
    def create_link_event(self, event, title, url):
        link_event = LinkEvent(event=event, title=title, url=url)
        link_event.save()
        return link_event

    def edit_link_event(self, link_event_id, event=None, title=None, url=None):
        link_event = LinkEvent.objects.get(id=link_event_id)
        if event:
            link_event.event = event
        if title:
            link_event.title = title
        if url:
            link_event.url = url
        link_event.save()
        return link_event

    def delete_link_event(self, link_event_id):
        link_event = LinkEvent.objects.get(id=link_event_id)
        link_event.delete()


def creating_link(request):
    link_event_editor = LinkEventEditor()
    form = None
    if request.method == 'POST':
        if 'create' in request.POST:
            form = LinkEventForm(request.POST)
            if form.is_valid():
                link_event_editor.create_link_event(**form.cleaned_data)
        elif 'edit' in request.POST:
            link_event_id = request.POST.get('link_event_id')
            form = LinkEventForm(request.POST)
            if form.is_valid():
                link_event_editor.edit_link_event(link_event_id, **form.cleaned_data)
        elif 'delete' in request.POST:
            link_event_id = request.POST.get('link_event_id')
            link_event_editor.delete_link_event(link_event_id)
    else:
        form = LinkEventForm()
    if form is None:
        form = LinkEventForm()
    link_events = LinkEvent.objects.all()
    context = {'form': form, 'link_events': link_events}
    return render(request, 'users/creating_link.html', context)


class EventEditor:
    def create_event(self, category, date_event, slug, title_event, text_event, place_realization,
                     illustration_event, brief_announcement, link_to_position):
        event = Event.objects.create(category=category, date_event=date_event, slug=slug, title_event=title_event,
                                     text_event=text_event, place_realization=place_realization,
                                     illustration_event=illustration_event, brief_announcement=brief_announcement,
                                     link_to_position=link_to_position)
        return event

    def edit_event(self, event_id, category=None, date_event=None, slug=None, title_event=None, text_event=None,
                   place_realization=None, illustration_event=None, brief_announcement=None, link_to_position=None):
        event = Event.objects.get(id=event_id)
        if category:
            event.category = category
        if date_event:
            event.date_event = date_event
        if slug:
            event.slug = slug
        if title_event:
            event.title_event = title_event
        if text_event:
            event.text_event = text_event
        if place_realization:
            event.place_realization = place_realization
        if illustration_event:
            event.illustration_event = illustration_event
        if brief_announcement:
            event.brief_announcement = brief_announcement
        if link_to_position:
            event.link_to_position = link_to_position
        event.save()
        return event

    def delete_event(self, event_id):
        event = Event.objects.get(id=event_id)
        event.delete()


def creating_events(request):
    event_editor = EventEditor()
    form = None
    if request.method == 'POST':
        if 'create' in request.POST:
            form = EventForm(request.POST, request.FILES)
            if form.is_valid():
                event_editor.create_event(**form.cleaned_data)
        elif 'edit' in request.POST:
            event_id = request.POST.get('event_id')
            form = EventForm(request.POST, request.FILES)
            if form.is_valid():
                event_editor.edit_event(event_id, **form.cleaned_data)
        elif 'delete' in request.POST:
            event_id = request.POST.get('event_id')
            event_editor.delete_event(event_id)
    else:
        form = EventForm()
    events = Event.objects.all()
    context = {'form': form, 'events': events}
    return render(request, 'users/creating_events.html', context)


def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_editing')
    else:
        form = EventForm(instance=event)

    context = {'form': form}
    return render(request, 'users/edit_event.html', context)


class TrainingEditor:
    def create_training(self, date_of_publication, slug, category, training_title, summary_training, full_training,
                        links_training, video_training, graphic_illustrations):
        training = Training(date_of_publication=date_of_publication, slug=slug, category=category,
                            training_title=training_title, summary_training=summary_training,
                            full_training=full_training, links_training=links_training, video_training=video_training,
                            graphic_illustrations=graphic_illustrations)
        training.save()
        return training

    def edit_training(self, training_id, date_of_publication=None, slug=None, category=None, training_title=None,
                      summary_training=None, full_training=None, links_training=None, video_training=None,
                      graphic_illustrations=None):
        training = Training.objects.get(id=training_id)
        if date_of_publication:
            training.date_of_publication = date_of_publication
        if slug:
            training.slug = slug
        if category:
            training.category = category
        if training_title:
            training.training_title = training_title
        if summary_training:
            training.summary_training = summary_training
        if full_training:
            training.full_training = full_training
        if links_training:
            training.links_training = links_training
        if video_training:
            training.video_training = video_training
        if graphic_illustrations:
            training.graphic_illustrations = graphic_illustrations
        training.save()
        return training

    def delete_training(self, training_id):
        training = Training.objects.get(id=training_id)
        training.delete()


def creating_training(request):
    training_editor = TrainingEditor()
    form = None
    if request.method == 'POST':
        if 'create' in request.POST:
            form = TrainingForm(request.POST, request.FILES)
            if form.is_valid():
                training_editor.create_training(**form.cleaned_data)
        elif 'edit' in request.POST:
            training_id = request.POST.get('training_id')
            form = TrainingForm(request.POST, request.FILES)
            if form.is_valid():
                training_editor.edit_training(training_id, **form.cleaned_data)
        elif 'delete' in request.POST:
            training_id = request.POST.get('training_id')
            training_editor.delete_training(training_id)
    else:
        form = TrainingForm()
    if form is None:
        form = TrainingForm()
    trainings = Training.objects.all()
    context = {'form': form, 'trainings': trainings}
    return render(request, 'users/creating_learning.html', context)


class CommentEditor:

    def delete_comment(self, comment_id):
        try:
            comment = Comments.objects.get(id=comment_id)
            comment.delete()
        except Comments.DoesNotExist:
            pass


def creating_comments(request):
    comment_editor = CommentEditor()
    if request.method == 'POST':
        if 'delete' in request.POST:
            comment_id = request.POST.get('comment_id')
            comment_editor.delete_comment(comment_id)
    comments = Comments.objects.all()
    context = {'comments': comments}
    return render(request, 'users/editing_comments.html', context)

from django.shortcuts import render, redirect
from .forms import EventFilePDFForm

def create_event_file_pdf(request):
    if request.method == 'POST':
        form = EventFilePDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    else:
        form = EventFilePDFForm()
    return render(request, 'users/create_event_file_pdf.html', {'form': form})