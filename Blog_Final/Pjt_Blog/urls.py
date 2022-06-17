from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('App_Blog.urls')),
    path('users/', include('App_Users.urls')),
    path('chats/', include('App_Chat.urls')),
    path('admin/', admin.site.urls, name='admin'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)