from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
                TodoViewSet,
                todo_create,
                todo_delete,
                todo_detail,
                todo_list,
                todo_update,
                )

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),

    # Template Views
    path('', todo_list, name='todo_list'),
    path('todo/<int:pk>/', todo_detail, name='todo_detail'),
    path('todo/new/', todo_create, name='todo_create'),
    path('todo/<int:pk>/edit/', todo_update, name='todo_update'),
    path('todo/<int:pk>/delete/', todo_delete, name='todo_delete'),
]
