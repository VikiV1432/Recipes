from django.urls import path
from .views import HomePageView, AddMenuPage, get_all_ingredients_data
urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('recipes/',AddMenuPage.as_view(), name="add-menu"),
    path('recipes/<slug:slug>',AddMenuPage.as_view(), name='edit-recipe'),
    path('api/ingredients', get_all_ingredients_data, name="ingredients-list"),
]