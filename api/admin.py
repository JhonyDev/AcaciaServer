from django.contrib import admin

from .models import *

admin.site.register(Photo)
admin.site.register(User)
admin.site.register(Liked)
admin.site.register(Interest)
