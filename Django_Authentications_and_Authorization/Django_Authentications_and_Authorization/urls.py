from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Django_Authentications_and_Authorization.demo.urls')),
]
