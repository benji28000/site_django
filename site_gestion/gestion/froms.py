from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','category','description','image']
        labels={'title':'Titre', 'category':'Catégorie','description':'Description'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':5}),
        }