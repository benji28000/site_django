from django.shortcuts import render
from gestion.models import Article
from gestion.froms import ArticleForm
from .models import Article

def home(request):
    list_articles=Article.objects.all()
    context={"list_articles":list_articles}
    return render(request,"index.html",context)

def detail(request,id_article):
    article=Article.objects.get(id=id_article)
    categoryy=article.category
    articles_en_relation=Article.objects.filter(category=categoryy)
    name_category=article.category
    return render(request,'detail.html',{"article":article,"aer":articles_en_relation,"name_cate":name_category})

def search(request):
    element=request.GET["article"]
    liste_articles=Article.objects.filter(title__contains=element)
    return render(request,"search.html",{"liste_article":liste_articles})

