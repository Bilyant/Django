from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', include('Django_User_and_Password_management.demo.urls')),
    path('auth/', include('Django_User_and_Password_management.app_auth.urls')),
]
