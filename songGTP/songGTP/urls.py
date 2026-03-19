"""
URL configuration for songGTP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from backend.views import get_user, create_user,update_user,delete_user,\
    get_prompt,create_library,create_prompt,create_song,update_library,update_prompt,\
    update_song,delete_song,delete_library,delete_prompt

urlpatterns = [
    path('admin/', admin.site.urls),
    # USER
    path("users/", get_user, name="users"),
    path("users/create/", create_user, name="create_user"),
    path("users/update/<int:user_id>/", update_user, name="update_user"),
    path("users/delete/<int:user_id>/", delete_user, name="delete_user"),

    # PROMPT
    path("prompt/", get_prompt, name="prompt"),
    path("prompt/create/", create_prompt, name="create_prompt"),
    path("prompt/update/<int:prompt_id>/", update_prompt, name="update_prompt"),
    path("prompt/delete/<int:prompt_id>/", delete_prompt, name="delete_prompt"),

    # SONG
    path("song/", get_song, name="song"),
    path("song/create/", create_song, name="create_song"),
    path("song/update/<int:song_id>/", update_song, name="update_song"),
    path("song/delete/<int:song_id>/", delete_song, name="delete_song"),

    # LIBRARY
    path("library/", get_library, name="library"),
    path("library/create/", create_library, name="create_library"),
    path("library/update/<int:library_id>/", update_library, name="update_library"),
    path("library/delete/<int:library_id>/", delete_library, name="delete_library"),
]
