from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

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
    body = json.loads(request.body)

    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

    user.username = body.get("name", user.username)

    user.save()

    return JsonResponse({"message": "updated"})


def delete_user(request, user_id):
    try:
        user = User.objects.get(user_id)
    except User.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

    user.delete()

    return JsonResponse({"message": "deleted"})