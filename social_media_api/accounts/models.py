from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name="following",
        blank=True
    )

    def follow(self, user):
        """Follow another user"""
        if user != self:
            self.following.add(user)

    def unfollow(self, user):
        """Unfollow another user"""
        self.following.remove(user)

    def is_following(self, user):
        return self.following.filter(id=user.id).exists()
