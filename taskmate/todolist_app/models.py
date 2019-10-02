from django.db import models

# Create your models here.

class TaskList(models.Model):
    Task = models.CharField(max_length = 300)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.Task +'--' + str(self.done)
