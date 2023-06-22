import datetime
from django.utils import timezone
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from training.models import Training
from event.models import Event
from event.models import Category ,EventFilePDF

def main(request):
    now = timezone.now()
    next_month = now + datetime.timedelta(days=7)
    two_weeks_from_now = now + datetime.timedelta(weeks=2)
    category_sport = Category.objects.get(name='Соревнования')
    events = Event.objects.filter(category=category_sport,date_event__gte=now, date_event__lte=next_month)
    training_lessons = Training.objects.all()
    two_weeks_ago = now - datetime.timedelta(weeks=2)
    two_weeks_from_now = now + datetime.timedelta(weeks=2)
    five_events = Event.objects.filter(date_event__gte=two_weeks_ago, date_event__lte=two_weeks_from_now).order_by(
        'date_event')[:5]
    event = Event.objects.order_by('-date_event').all()
    paginator = Paginator(event,10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'main/news.html',{
        'page_obj': page_obj,
        'training_lessons':training_lessons,
        'event':event,
        'events':events,
        'next_month':next_month,
        'five_events':five_events,

    })


def logout_user(request):
    logout(request)
    return redirect('main:main')


def document(request):
    category_doc = Category.objects.get(name='Документы')
    doc = EventFilePDF.objects.filter(category=category_doc)
    return render(request,'main/doc.html',doc)

from django.contrib.auth.models import Group

def group_check(request):
    if request.user.is_authenticated:
        is_redactor = Group.objects.filter(name='Redactor', user=request.user).exists()
    else:
        is_redactor = False
    return {'is_redactor': is_redactor}