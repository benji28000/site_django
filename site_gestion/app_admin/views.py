from django.shortcuts import render,redirect
from gestion.models import Article
from gestion.froms import ArticleForm
from django.views.generic.edit import UpdateView,CreateView,DeleteView

def dashboard(request):
    return render(request,'dashboard.html')

def user_articles(request):
    if not request.user.is_authenticated:
        return redirect('home')
    else:
        liste_articles=Article.objects.filter(user=request.user)
        return render(request,'my_articles.html',{'liste_articles':liste_articles})
    
class AddArticle(CreateView):
    model=Article
    form_class = ArticleForm
    template_name ="add-article.html"
    success_url='../my_articles'

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class UpdateArticle(UpdateView):
    model=Article
    form_class=ArticleForm
    template_name='app_admin/formulaire_article.html'
    success_url='/myadmin/my_articles/'

class DeleteArticle(DeleteView):
    model=Article
    success_url='/myadmin/my_articles/'
    template_name='supprimer_article.html'