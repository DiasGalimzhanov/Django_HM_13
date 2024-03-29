from django.urls import path
from .views import TodoList, TodoCreate, TodoUpdate, TodoDelete, TodoDetail

urlpatterns = [
    path('', TodoList.as_view(), name='home'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('update/<int:pk>/', TodoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name='delete'),
    path('detail/<int:pk>/', TodoDetail.as_view(), name='detail'),
]
