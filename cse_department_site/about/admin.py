from django.contrib import admin

from .models import Gallery, Club, Message

# Register your models here.
admin.site.register(Gallery)
admin.site.register(Club)
admin.site.register(Message)