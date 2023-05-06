import datetime
from django.utils import timezone
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from training.models import Training
from event.models import Event
from event.models import Category

def main(request):
    now = timezone.now()
    next_month = now + datetime.timedelta(days=7)
    category_sport = Category.objects.get(name='Соревнования')
    events = Event.objects.filter(category=category_sport,date_event__gte=now, date_event__lte=next_month)
    training_lessons = Training.objects.all()
    five_events = Event.objects.order_by('-date_event').all()[:5]
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