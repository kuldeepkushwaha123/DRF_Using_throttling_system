from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Messages(models.Model):
    message=models.TextField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,to_field="username",related_name="created_by")
    def __str__(self):
        return "username : "+str(self.user)+"  message : "+str(self.message[:10])











