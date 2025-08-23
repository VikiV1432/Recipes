from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, View
from .models import RecipeType, Cuisine, Recipe, Ingredient, RecipeIngredient, Unit
from django.urls import reverse_lazy
from .forms import RecipeForm
from django.http import JsonResponse
import json

# Create your views here.
class HomePageView(TemplateView):
    template_name="main/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe_types"] = RecipeType.objects.all()
        context["cuisines"] = Cuisine.objects.all()
        return context
    

class AddMenuPage(View):
    model=Recipe
    template_name='main/add-menu.html'
    success_url=reverse_lazy('home')
    form_class=RecipeForm
    def get(self, request):
        ingredients=Ingredient.objects.all()
        units=Unit.objects.all()
        form=self.form_class()
        return render(request, self.template_name, context={'form':form,'ingredients':ingredients,'units':units})
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def post(self, request):
        ingredients= request.POST.get('ingredients')
        form= RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe= form.save(commit=False)
            recipe.user= request.user
            recipe.save()
            if ingredients is not None:
                ingredients=json.loads(ingredients)
                for ingredient in ingredients:
                    name= ingredient.get('ingredient')
                    unit= ingredient.get('unit')
                    input= ingredient.get('input')
                    RecipeIngredient.objects.create(
                        ingredient=Ingredient.objects.get(title=name),
                        unit=Unit.objects.get(title=unit),
                        quantity=float(input),
                        recipe=recipe
                    )
            return redirect('home')
        print(form.errors)
        ingredients=Ingredient.objects.all()
        units=Unit.objects.all()
        return render(request, self.template_name, context={'form':form,'ingredients':ingredients,'units':units})

    
def get_all_ingredients_data(request):
    ingredients=list(Ingredient.objects.values())
    units=list(Unit.objects.values())
    return JsonResponse({'ingredients':ingredients,'units':units})