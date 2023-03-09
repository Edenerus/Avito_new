from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import user
from user.views.user import Logout


urlpatterns = [
    path('', user.UserListView.as_view()),
    path('<int:pk>/', user.UserDetailView.as_view()),
    path('create/', user.UserCreateView.as_view()),
    path('<int:pk>/update/', user.UserUpdateView.as_view()),
    path('<int:pk>/delete/', user.UserDeleteView.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', Logout.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
