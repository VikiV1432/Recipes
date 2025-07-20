from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient,Cuisine,RecipeType,Unit


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display=('title','description','created_at','updated_at')
    ordering=('-created_at','title')
    search_fields=('title','description')
    list_filter=('created_at','updated_at')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display=('title','created_at','updated_at')
    ordering=('-created_at','title')
    search_fields=('title',)
    list_filter=('created_at','updated_at')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display=('title','created_at','updated_at','cuisine','user')
    ordering=('-created_at','title')
    search_fields=('title','cuisine','user')
    list_filter=('created_at','updated_at')


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display=('ingredient', 'recipe')
    ordering=('ingredient',)
    search_fields=('ingredient','recipe')


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display=('title','created_at','updated_at')
    ordering=('-created_at','title')
    search_fields=('title',)
    list_filter=('created_at','updated_at')


@admin.register(RecipeType)
class RecipeTypeAdmin(admin.ModelAdmin):
    list_display=('title','created_at','updated_at')
    ordering=('-created_at','title')
    search_fields=('title',)
    list_filter=('created_at','updated_at')
# Register your models here.

