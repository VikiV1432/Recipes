from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, View, UpdateView, DeleteView
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
    def get(self, request, slug=None):
        recipes=Recipe.objects.filter(slug=slug)
        if len(recipes)>0:
            recipe=recipes[0]
        else:
            recipe=None
        ingredients=Ingredient.objects.all()
        units=Unit.objects.all()
        form=self.form_class()
        if recipe:
            form=self.form_class(instance=recipe)
        return render(request, self.template_name, context={'form':form,'ingredients':ingredients,'units':units})
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def post(self, request, slug=None):
        ingredients= request.POST.get('ingredients')
        if slug:
            recipe=get_object_or_404(Recipe,slug=slug)
            form=RecipeForm(request.POST, request.FILES, instance=recipe)
        else:
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
        else:
            return JsonResponse(form.errors, status=400)
       


    
def get_all_ingredients_data(request):
    ingredients=list(Ingredient.objects.values())
    units=list(Unit.objects.values())
    return JsonResponse({'ingredients':ingredients,'units':units})