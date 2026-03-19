from django.db import models

# Create your models here.
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

class Prompt(models.Model):
    song_name = models.CharField(max_length=50)
    song_genre = models.CharField(max_length=20, choices=Genre.choices)
    song_mood = models.CharField(max_length=20, choices=Mood.choices)
    song_base_singer = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    lyrics = models.TextField(blank= True)
    keywords = models.TextField(blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
