"""goticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
	# homepage
	path('', include('home.urls')),

	# admin
    path('admin/', admin.site.urls),

	# auth
	path('auth/', include('djoser.urls')),
	path('auth/users/', include('djoser.urls'), name='create_account'),
	path('events/', include('events.urls')),
	path('api-auth/', include('rest_framework.urls')),

	# accounts
    path('store/', views.store , name='store'),
	path('login.html', views.login, name='login'),
	path('sign_up.html', views.signup, name='signup'),
	path('profiles.html', views.profile, name='profile'),

	# jwt
	path('auth/jwt/create',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('auth/jwt/refresh',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
	path('auth/jwt/verify/',
		jwt_views.TokenVerifyView.as_view(),
		name='token_verify'),
]
