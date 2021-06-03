from django.urls import path
from .views import StockActivityListView, StockActivityDetailView

urlpatterns = [
    path('', StockActivityListView.as_view()),
    path('<int:pk>/', StockActivityDetailView.as_view()),
]