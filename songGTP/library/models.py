from django.db import models
from user.models import User

# Create your models here.
class Library(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="library_user_id")
    created_at = models.DateTimeField(auto_now_add=True)