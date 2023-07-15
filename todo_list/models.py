from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime

# Create your models here.

class Task(models.Model):
    """Model definition for Task."""
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)
    complete=models.BooleanField(default=False)
    creat_at=models.DateTimeField(verbose_name=_("Created At"), auto_now_add=True)

    class Meta:
        """Meta definition for Task."""

        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering=['complete']

