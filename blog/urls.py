from django.urls import path
from blog.views import blogData, blogHome, displayContent

urlpatterns=[
    path('create_blog/', blogData),
    path('blog_home/', blogHome),
    path('display_content/<int:slug>/', displayContent),
]