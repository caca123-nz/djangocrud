from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Main(models.Model):
  title = models.CharField(max_length=200)
  excerpt = models.TextField(null=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='main')
  slug = models.SlugField(max_length=100, unique=True)
  update = models.DateTimeField(auto_now=True)
  published = models.DateTimeField(default=timezone.now)

  def get_absolute_url(self):
    return reverse('mainapp:detail', kwargs={'slug': self.slug})
  
  class Meta:
    ordering = ['-published']

  def __str__(self):
    return self.title
