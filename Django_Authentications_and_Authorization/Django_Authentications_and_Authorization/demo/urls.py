from django.urls import path
from Django_Authentications_and_Authorization.demo.views import index, login_user, logout_user

urlpatterns = (
    path(route='', view=index, name='index'),
    path(route='login/', view=login_user, name='login_user'),
    path(route='logout/', view=logout_user, name='logout_user'),
)
