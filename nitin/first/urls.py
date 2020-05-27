from django.urls import path,include
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('login',views.login,name='login'),
	path('register',views.register,name='register'),
	path('logout',views.logout,name='logout'),
	
    path('oauth/',include('social_django.urls',namespace='social')),
	
]
