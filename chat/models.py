from django.db import models
from django.contrib.auth.models import User
class ChatGroup(models.Model):
    group_name = models.CharField(max_length=120)
    onlines_users = models.ManyToManyField(User, related_name="online_in_groups", blank=True)
    def __str__(self):
        return self.group_name
class GroupMessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name="chat_messages", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.author.username} ({self.group})"
    class Meta:
        ordering = ["created"]