from django.urls import path
from my_app.views import TodoView
from .views import ProtectedView

urlpatterns = [
    path('todo', TodoView.as_view()),
    path('api/protected/', ProtectedView.as_view(), name='protected'),
    ]