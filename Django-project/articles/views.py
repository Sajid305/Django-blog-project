from django.shortcuts import render
from articles.models import Article
# Create your views here.



def article_list(request):
    articles = Article.objects.all().order_by('dete')
    
    return render(request, 'index.html',{'articles':articles})