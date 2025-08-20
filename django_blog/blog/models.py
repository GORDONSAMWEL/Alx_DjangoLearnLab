# Step 3: Define Blog Models
# Model Specifications:
# Create a model Post in blog/models.py with the following fields:
# title: models.CharField(max_length=200)
# content: models.TextField()
# published_date: models.DateTimeField(auto_now_add=True)
# author: models.ForeignKey to Django’s User model, with a relation to handle multiple posts by a single author.
# Run the migrations to create the model in the database: bash python manage.py makemigrations blog python manage.py migrate


from django.db import models
from django.contrib.auth.models import User




from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
     photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
     bio = models.TextField(blank=True)
     updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
   return f"Profile({self.user.username})"


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

