from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, View
from .models import RecipeType, Cuisine, Recipe, Ingredient, RecipeIngredient, Unit
from django.urls import reverse_lazy
from .forms import RecipeForm
from django.http import JsonResponse

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

    
def get_all_ingredients_data(request):
    ingredients=list(Ingredient.objects.values())
    units=list(Unit.objects.values())
    return JsonResponse({'ingredients':ingredients,'units':units})