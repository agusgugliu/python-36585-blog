from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from App_Chat import views

urlpatterns = [
    path('chat/', views.blogChat, name='chat'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
