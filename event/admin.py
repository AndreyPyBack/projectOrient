from django.contrib import admin

# Register your models here.
from .models import Event,Comments,LinkEvent,Category
# Register your models here.

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Comments)
admin.site.register(LinkEvent)