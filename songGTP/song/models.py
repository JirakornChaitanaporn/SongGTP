from django.db import models
from library.models import Library
from prompt.models import Prompt

# Create your models here.
class Status(models.TextChoices):
    PUBLIC = 'public', 'Public'
    PRIVATE = 'private', 'Private'

class Generation(models.TextChoices):
    GENERATING = 'generating', 'Generating'
    GENERATED = 'generated', 'Generated'
    ERROR = 'error', 'Error'

class Song(models.Model):
    prompt = models.OneToOneField(Prompt,on_delete=models.CASCADE, related_name="song_prompt_id")
    library = models.ForeignKey(Library,on_delete=models.CASCADE, db_column="library_id", related_name="song_library_id")
    song_name = models.CharField(max_length=50)
    shared_link = models.CharField(max_length=255, blank=True)
    sharing_status = models.CharField(max_length=20, choices=Status.choices)
    generation_status = models.CharField(max_length=20, choices=Generation.choices)
    song_url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)