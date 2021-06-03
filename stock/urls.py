from django.urls import path
from .views import StockListView, StockDetailView, GenerateNewStockNumberIndex

urlpatterns = [
    path('', StockListView.as_view()),
    path('new-index/', GenerateNewStockNumberIndex.as_view()),
    path('<pk>/', StockDetailView.as_view()),
]