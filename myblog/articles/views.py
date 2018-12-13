from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Articles
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def articles_list(request):
    article = Articles.objects.all().order_by('date')
    return render(request,'articles/article.html',{'article':article})

def article_detail(request,slug):
    # return HttpResponse(slug)
    articles = Articles.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':articles})

@login_required(login_url='/account/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticles(request.POST,request.FILES)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticles()
    return render(request,'articles/article_create.html',{'form':form})



