# from django.db import models

# # Create your models here.
# # models.py
# from django.db import models
# from django.contrib.auth.models import User

# class Interest(models.Model):
#     sender = models.ForeignKey(User, related_name='sent_interests', on_delete=models.CASCADE)
#     recipient = models.ForeignKey(User, related_name='received_interests', on_delete=models.CASCADE)
#     message = models.TextField()
#     accepted = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)

# class ChatMessage(models.Model):
#     chat_id = models.ForeignKey(Interest, on_delete=models.CASCADE)
#     sender = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
# models.py
from django.db import models
from django.contrib.auth.models import User

class Interest(models.Model):
    sender = models.ForeignKey(User, related_name='sent_interests', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_interests', on_delete=models.CASCADE)
    message = models.TextField()
    accepted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class ChatMessage(models.Model):
    chat_id = models.ForeignKey(Interest, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
