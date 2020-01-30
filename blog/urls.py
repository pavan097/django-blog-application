from django.urls import path
from blog.views import blogData, blogHome, displayContent, getData

urlpatterns=[
    path('create_blog/', blogData),
    path('blog_home/', blogHome),
    path('display_content/<int:slug>/', displayContent),
    path('getData/', getData, name='getData')
]