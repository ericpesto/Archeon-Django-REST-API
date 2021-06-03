from django.urls import path
from .views import NameListView, NameDetailView

urlpatterns = [
    path('', NameListView.as_view()),
    path('<int:pk>/', NameDetailView.as_view())
]