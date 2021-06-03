from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.exceptions import NotFound
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Stock
from .serializers.common import StockSerializer

from django.db.models import Max

# Create your views here.

class StockListView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, _request):
        stock_items = Stock.objects.all() 
        serialized_stock_items = StockSerializer(stock_items, many=True)
        print("✅ all stock items found")
        return Response(serialized_stock_items.data, status=status.HTTP_200_OK)

    def post(self, request):
        stock_item_to_add = StockSerializer(data=request.data)
        if stock_item_to_add.is_valid():
            stock_item_to_add.save()
            print("✅ stock item created")
            return Response(stock_item_to_add.data, status=status.HTTP_201_CREATED)
        return Response(stock_item_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class StockDetailView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_stock_item(self, pk):
        try:
            print(f"✅ stock item ({pk}) found")
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            print("🆘 stock item not found")
            raise NotFound(detail="🆘 stock item not found")
    
    def get(self, _request, pk):
        stock_item = self.get_stock_item(pk=pk)
        serialized_stock_item = StockSerializer(stock_item)
        return Response(serialized_stock_item.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        stock_item_to_edit = self.get_stock_item(pk=pk)
        updated_stock_item = StockSerializer(stock_item_to_edit, data=request.data)
        if updated_stock_item.is_valid():
            updated_stock_item.save()
            print(f"✅ stock item ({pk})  edited")
            return Response(updated_stock_item.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_stock_item.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        stock_item_to_delete = self.get_stock_item(pk=pk)
        stock_item_to_delete.delete()
        print(f"✅ stock item ({pk})  deleted")
        return Response(status=status.HTTP_204_NO_CONTENT)

class GenerateNewStockNumberIndex(APIView):
    def get(self, _request):
        highest_stock_num = Stock.objects.all().aggregate(Max('stock_num'))
        next_highest_index = highest_stock_num["stock_num__max"] + 1
        print(f"✅ new stock number generated: {next_highest_index} ")
        return Response(next_highest_index, status=status.HTTP_200_OK)