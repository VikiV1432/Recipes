from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

# Create your models here.
class Unit(models.Model):
    title=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    description=models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.title



class RecipeType(models.Model):
    title=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="types/", null=True, blank=True)
    def __str__(self):
        return self.title



class Cuisine(models.Model):
    title=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="cuisines/", null=True, blank=True)
    def __str__(self):
        return self.title



class Ingredient(models.Model):
    title=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="ingredients/", null=True, blank=True)
    def __str__(self):
        return self.title



class Recipe(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(max_length=700, null=True, blank=True)
    image=models.ImageField(upload_to="recipes/", null=True, blank=True)
    type=models.ForeignKey(RecipeType,on_delete=models.SET_NULL, null=True, related_name="recipes")
    cuisine=models.ForeignKey(Cuisine,on_delete=models.SET_NULL, null=True, related_name="recipes")
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="recipes")
    video_link=models.URLField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    slug=models.SlugField(unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug=slugify(self.title)
            slug=base_slug
            counter=1
            while Recipe.objects.filter(slug=slug).exists():
                slug=f"{base_slug}-{counter}"
                counter+=1
            self.slug=slug
        return super().save(*args, **kwargs)
    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    ingredient=models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipes_ingredients")
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    quantity=models.FloatField()
    unit=models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, related_name="recipes_ingredients")
    def __str__(self):
        return f"{self.ingredient.title} ---> {self.recipe.title}"
