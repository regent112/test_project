from main.models import *
from django.contrib.auth.models import User

class Update(models.Model):
  author = models.ForeignKey(User, on_delete = models.CASCADE)
  text = models.TextField()
