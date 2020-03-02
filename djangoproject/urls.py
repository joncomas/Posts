from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [    
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    url(r'^$', include('posts.urls')),
]
