from django.db import models
from django.contrib.auth.models import User

class WardrobeItem(models.Model):
    CATEGORY_CHOICES = [
        ('top', 'Top'),
        ('pants', 'Pants'),
        ('shoes', 'Shoes'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='wardrobe/')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s {self.category}"
