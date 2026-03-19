from django.db import models

# Create your models here.
# Enum
class Mood(models.TextChoices):
    HAPPY = 'happy', 'Happy'
    SAD = 'sad', 'Sad'
    ROMANTIC = 'romantic', 'Romantic'
    ANGRY = 'angry', 'Angry'
    ENERGETIC = 'energetic', 'ENERGETIC'
    CALM = 'calm', 'Calm'
    
class Genre(models.TextChoices):
    POP = 'pop', 'Pop'
    ROCK = 'rock', 'Rock'
    HEAVY_METAL = 'heavy_metal', 'Heavy_metal'
    SOFT_ROCK = 'soft_rock', 'Soft_rock'
    POP_ROCK = 'pop_rock', 'Pop_rock'
    COUNTRY = 'country', 'Country'
    
class Status(models.TextChoices):
    PUBLIC = 'public', 'Public'
    PRIVATE = 'private', 'Private'
    
class Generation(models.TextChoices):
    GENERATING = 'generating', 'Generating'
    GENERATED = 'generated', 'Generated'
    ERROR = 'error', 'Error'
    
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Library(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="library_user_id")
    created_at = models.DateTimeField(auto_now_add=True)
    
class Prompt(models.Model):
    song_name = models.CharField(max_length=50)
    song_genre = models.CharField(max_length=20, choices=Genre.choices)
    song_mood = models.CharField(max_length=20, choices=Mood.choices)
    song_base_singer = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    lyrics = models.TextField(blank= True)
    keywords = models.TextField(blank= True)
    created_at = models.DateTimeField(auto_now_add=True)

class Song(models.Model):
    prompt = models.OneToOneField(Prompt,on_delete=models.CASCADE, related_name="song_prompt_id")
    library = models.ForeignKey(Library,on_delete=models.CASCADE, db_column="library_id", related_name="song_library_id")
    song_name = models.CharField(max_length=50)
    shared_link = models.CharField(max_length=255, blank=True)
    sharing_status = models.CharField(max_length=20, choices=Status.choices)
    generation_status = models.CharField(max_length=20, choices=Generation.choices)
    song_url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Folder(models.Model):
    pass
    