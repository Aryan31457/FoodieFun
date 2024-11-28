from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Recipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    recipe_name = models.CharField(max_length=255)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipes")

    
    def __str__(self):
        return f"{self.id} - {self.recipe_name} + {self.user}"
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos/', default='default.jpg')
    food_points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    


