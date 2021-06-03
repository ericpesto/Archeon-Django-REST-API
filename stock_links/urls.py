from django.urls import path
from .views import StockLinkListView, StockLinkDetailView

urlpatterns = [
    path('', StockLinkListView.as_view()),
    path('<int:pk>/', StockLinkDetailView.as_view()),

]