from django.urls import path
from .views import BoxList, BoxUpdate, MyBoxList , BoxDelete,RegisterView, LoginView, UserDetailView

urlpatterns = [
    path('boxes/', BoxList.as_view(), name='box-list'),
    path('boxes/<int:pk>/', BoxUpdate.as_view(), name='box-update'),
    path('my-boxes/', MyBoxList.as_view(), name='my-box-list'),
    path('my-boxes/<int:pk>/', BoxDelete.as_view(), name='box-delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
]