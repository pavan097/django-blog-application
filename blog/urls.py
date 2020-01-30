from django.urls import path
from blog.views import blogData, blogHome, displayContent, getData

urlpatterns=[
    path('create_blog/', blogData, name='blogData'),
    path('blog_home/', blogHome, name='blogHome'),
    path('display_content/<int:slug>/', displayContent, name='display_content'),
    path('getData/', getData, name='getData')
]