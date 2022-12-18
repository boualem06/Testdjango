from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', include('main.urls')), # main will be the name of your app
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
]