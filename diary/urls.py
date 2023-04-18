from django.urls import path
from .views import create_profile, landing, entry_list, entry_detail, entry_create, entry_update, entry_delete
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', entry_list, name='entry_list'),
    path('<int:entry_id>/', entry_detail, name='entry_detail'),
    path('new/', entry_create, name='entry_create'),
    path('<int:entry_id>/edit/', entry_update, name='entry_update'),
    path('<int:entry_id>/delete/', entry_delete, name='entry_delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('landing/', landing, name='landing'),
    path('profile/create/', create_profile, name='create_profile'),
]
