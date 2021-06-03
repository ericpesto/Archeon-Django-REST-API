from django.urls import path
from .views import ActivityDefinitionListView, ActivityDefinitionDetailView

urlpatterns = [
    path('', ActivityDefinitionListView.as_view()),
    path('<int:pk>/', ActivityDefinitionDetailView.as_view()),
]