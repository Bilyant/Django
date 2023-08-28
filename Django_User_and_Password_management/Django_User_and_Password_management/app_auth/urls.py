from django.urls import path
from Django_User_and_Password_management.app_auth.views import RegisterUserView, LoginUserView, LogoutUserView, \
    ProfileDetailsUserView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('profile-details/<int:pk>/', ProfileDetailsUserView.as_view(), name='details user'),
)
