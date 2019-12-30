from django.shortcuts import render
from blog.models import BlogContent
from django.http import HttpResponse
from datetime import datetime

def blogData(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        created_on = datetime.now()
        updated_on = datetime.now()
        print('data is :',title, content, category)
        d = BlogContent(title=title, content=content, category=category, created_on=created_on, updated_on=updated_on)
        d.save()
        return HttpResponse('Success')
    return render(request, 'content_create.html', {})

def blogHome(request):
    data = BlogContent.objects.all()
    return render(request, 'blog_home.html', {'data':data})

def displayContent(request):
    return HttpResponse('success')