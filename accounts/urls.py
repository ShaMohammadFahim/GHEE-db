from django.urls import path ,include
from .views import SignupView, UserProfileView # UserProfileView add korun
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
   
    path('signup/', SignupView.as_view(), name='signup'),
    
  
    path('login/', TokenObtainPairView.as_view(), name='login'),
    

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    path('profile/', UserProfileView.as_view(), name='user-profile'),

    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]