from django.urls import path
from accounts import views
urlpatterns = [
    path('register/',views.RegisterView.as_view(), name="register"),
    path('login/',views.login_view,name="login"),
    path('base/',views.base, name="base"),
    path('test/',views.base, name="base"),
    path('home/',views.home, name="home"),
    path('logout/',views.logout_view, name='logout'),
  
]
