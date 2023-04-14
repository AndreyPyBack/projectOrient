from django.contrib import admin

# Register your models here.
from .models import Event,Comments,LinkEvent
# Register your models here.

admin.site.register(Event)
admin.site.register(Comments)
admin.site.register(LinkEvent)