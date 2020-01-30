from django.shortcuts import render
from blog.models import BlogContent
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core import serializers

@login_required
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

@login_required
def blogHome(request):
    data = BlogContent.objects.all()
    return render(request, 'blog_home.html', {'data':data})

def displayContent(request, slug):
    d = BlogContent.objects.get(id=slug)
    return render(request, 'display_content.html', {'d':d})

def getData(request):
    if request.method == "GET":
        data = BlogContent.objects.all()
        data = serializers.serialize('json', data)
        # return JsonResponse(data, safe=False)
        return HttpResponse(data, content_type='application/json')