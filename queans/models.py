from django.db import models

# Create your models here.
class Questions(models.Model):

    title = models.CharField(max_length=500 ,blank=True)
    link = models.URLField()
    count = models.CharField(max_length=15)
    answered = models.CharField(max_length=6)
    view_count = models.CharField(max_length=15)
    asked_by = models.URLField()

    def __str__(self):
        return self.title
        