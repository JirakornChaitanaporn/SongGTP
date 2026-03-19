from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import User, Prompt, Library, Song
# Create your views here.

def get_user(request):
    users = User.objects.all()

    return render(request, "users.html", {"users": users})

def create_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")

        User.objects.create(
            username=username,
            email=email
        )

    return redirect("users")
    
def update_user(request, user_id):
    if request.method == "POST":
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return redirect("users")

        user.username = request.POST.get("username", user.username)
        user.email = request.POST.get("email", user.email)

        user.save()

    return redirect("users")

def delete_user(request, user_id):
    if request.method == "POST":
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return redirect("users")

        user.delete()

    return redirect("users")

#prompt
def get_prompt(request):
    prompt = Prompt.objects.all()

    return render(request, "prompt.html", {"prompt": prompt})

def create_prompt(request):
    if request.method == "POST":
        song_genre = request.POST.get("song_name")
        song_mood = request.POST.get("song_mood")
        song_base_singer = request.POST.get("song_base_singer")
        description = request.POST.get("description")
        lyrics = request.POST.get("lyrics")
        keywords = request.POST.get("keywords")


        Prompt.objects.create(
            song_genre=song_genre,
            song_mood=song_mood,
            song_base_singer=song_base_singer,
            description=description,
            lyrics=lyrics,
            keywords=keywords
        )

    return redirect("prompt")
    
def update_prompt(request, prompt_id):
    if request.method == "POST":
        try:
            prompt = Prompt.objects.get(pk=prompt_id)
        except Prompt.DoesNotExist:
            return redirect("prompt")

        prompt.song_genre = request.POST.get("song_name")
        prompt.song_mood = request.POST.get("song_mood")
        prompt.song_base_singer = request.POST.get("song_base_singer")
        prompt.description = request.POST.get("description")
        prompt.lyrics = request.POST.get("lyrics")
        prompt.keywords = request.POST.get("keywords")

        prompt.save()

    return redirect("prompt")

def delete_prompt(request, prompt_id):
    if request.method == "POST":
        try:
            prompt = Prompt.objects.get(pk=prompt_id)
        except Prompt.DoesNotExist:
            return redirect("prompt")

        prompt.delete()

    return redirect("prompt")

#song
def get_song(request):
    song = Song.objects.all()

    return render(request, "song.html", {"song": song})

def create_song(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        library = request.POST.get("library")
        song_name = request.POST.get("song_name")
        shared_link = request.POST.get("shared_link")
        sharing_status = request.POST.get("sharing_status")
        generation_status = request.POST.get("generation_status")
        song_url = request.POST.get("song_url")

        Song.objects.create(
            prompt=prompt,
            library=library,
            song_name=song_name,
            shared_link=shared_link,
            sharing_status=sharing_status,
            generation_status=generation_status,
            song_url=song_url
        )

    return redirect("song")
    
def update_song(request, song_id):
    if request.method == "POST":
        try:
            song = Song.objects.get(pk=song_id)
        except Song.DoesNotExist:
            return redirect("song")

        song.prompt = request.POST.get("prompt")
        song.library = request.POST.get("library")
        song.song_name = request.POST.get("song_name")
        song.shared_link = request.POST.get("shared_link")
        song.sharing_status = request.POST.get("sharing_status")
        song.generation_status = request.POST.get("generation_status")
        song.song_url = request.POST.get("song_url")

        song.save()

    return redirect("song")

def delete_song(request, song_id):
    if request.method == "POST":
        try:
            song = Song.objects.get(pk=song_id)
        except Song.DoesNotExist:
            return redirect("song")

        song.delete()

    return redirect("song")


#library
def get_library(request):
    library = Library.objects.all()

    return render(request, "library.html", {"library": library})

def create_library(request):
    if request.method == "POST":
        user = request.POST.get("user")

        Library.objects.create(
            user=user,
        )

    return redirect("library")
    
def update_library(request, library_id):
    if request.method == "POST":
        try:
            library = Library.objects.get(pk=library_id)
        except Library.DoesNotExist:
            return redirect("library")

        library.user = request.POST.get("user")

        library.save()

    return redirect("library")

def delete_library(request, library_id):
    if request.method == "POST":
        try:
            library = Library.objects.get(pk=library_id)
        except Library.DoesNotExist:
            return redirect("library")

        library.delete()

    return redirect("library")
