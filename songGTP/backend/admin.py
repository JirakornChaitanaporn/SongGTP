from django.contrib import admin
from .models import User, Prompt, Library, Song

# Register your models here.
admin.site.register(User)
admin.site.register(Prompt)
admin.site.register(Library)
admin.site.register(Song)