from django.urls import path
from App_Blog import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.aboutAuthor, name='about'),
    path('blog/', views.BlogList.as_view(), name='notas_list'),
    path('new_blog/', views.BlogCreate.as_view(), name='notas_create'),
    path('details/<pk>/', views.BlogDetail.as_view(), name='notas_detail'),
    path('edit/<pk>/', views.BlogUpdate.as_view(), name='notas_update'),
    path('delete/<pk>/', views.BlogDelete.as_view(), name='notas_delete'),
    path('login/', views.BlogLogin.as_view(), name='user_login'),
    path('logout/', views.BlogLogout.as_view(), name='user_logout'),
]