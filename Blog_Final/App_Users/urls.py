from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from App_Users import views

urlpatterns = [
    path('new_user/', views.SignUpView.as_view(), name='user_signup'),
    path('profile/<pk>/', views.BloggerProfile.as_view(), name='user_profile'),
    path('edit/<pk>/', views.BloggerUpdate.as_view(), name ='user_edit'),
    path('avatar/', views.addAvatar, name='add_avatar'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
