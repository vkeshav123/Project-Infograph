from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Facts(models.Model):
    title = models.CharField(max_length = 50)
    facts = models.CharField(max_length = 300)
    date_of_fact = models.DateTimeField(default = timezone.now)

    def get_absolute_url(self):
        return reverse("article")
    
    def __str__(self):
        return self.title

class QNA(models.Model):
    title = models.ForeignKey(Facts, on_delete = models.CASCADE)
    q = models.CharField(max_length=200)
    a = models.TextField()
    date_of_qna = models.DateTimeField(default = timezone.now)

    def get_absolute_url(self):
        return reverse("article")
    
    def __str__(self):
        self.q