from django.contrib import admin

# Register your models here.
from .models import Event,Comments,LinkEvent,Category,EventImg,EventPDF,EventFilePDF
# Register your models here.

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Comments)
admin.site.register(LinkEvent)
admin.site.register(EventPDF)
admin.site.register(EventFilePDF)