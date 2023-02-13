from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Mémo:  Pour bien initialiser la clef étrangère Article.category j'ai dans le shell fait les commandes : from gestion.models import Category | Category.objects.create(name='uncategorized') | python manage.py make migrations | python manage.py migrate
class Category(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to='media',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("my-articles")
    
