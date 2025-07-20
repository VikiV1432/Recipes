from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    description=forms.CharField(required=False, widget=forms.Textarea(attrs={'class':"field", "placeholder":'Description'}))
    title=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':"field",  "placeholder":'Title'}))
    video_link=forms.URLField(required=False, widget=forms.TextInput(attrs={'class':"field",  "placeholder":'Video Link'}))

    class Meta:
        model=Recipe
        fields=['image','title','description','type','cuisine','video_link']
        widgets={
            'type':forms.Select(attrs={'class':"field",}),
            'cuisine':forms.Select(attrs={'class':"field",})
        }


