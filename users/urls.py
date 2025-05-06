from django.urls import path
from .views import RegisterView, UserLoginView, ProfileEditView, activate
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/edit/', ProfileEditView.as_view(), name='edit_profile'),
    path('activate/<str:token>/', activate, name='activate'),
]

