from django.contrib.auth import views
from django.urls import path
from .views import (DeleteUser,auth_register,EditUserDetail,signin,ListDetail,listuserdetail)
from django.contrib.auth.views import LogoutView
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'userapp'
urlpatterns =[
    path('login/',signin,name='auth-login'),
    path('api/',ListDetail.as_view(),name='api'),
    path('logout/',LogoutView.as_view(template_name='userapp/signout.html'),name='auth-logout'),
    path('register/',auth_register,name='auth-register'),
    path('',listuserdetail,name='home'),
    path('edit/<int:pk>',EditUserDetail.as_view(),name='edit'),
    path('delete/<int:pk>',DeleteUser.as_view(),name='delete'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]