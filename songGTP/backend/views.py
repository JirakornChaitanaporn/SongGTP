from django.shortcuts import render, redirect

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
