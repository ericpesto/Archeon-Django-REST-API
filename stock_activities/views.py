from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.exceptions import NotFound
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.

from .models import StockActivity
from .serializers.common import StockActivitySerializer

class StockActivityListView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, _request):
        stock_activities = StockActivity.objects.all()
        serialized_stock_activities = StockActivitySerializer(stock_activities, many=True)
        print("✅ all stock activities found")
        return Response(serialized_stock_activities.data, status=status.HTTP_200_OK)

    
    def post(self, request):
        stock_activity_to_add = StockActivitySerializer(data=request.data)
        if stock_activity_to_add.is_valid():
            stock_activity_to_add.save()
            print("✅ stock activitiy added")
            return Response(stock_activity_to_add.data, status=status.HTTP_201_CREATED)
        return Response(stock_activity_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class StockActivityDetailView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_stock_activity(self, pk):
        try:
            print(f"✅ stock activity ({pk}) found")
            return StockActivity.objects.get(pk=pk)
        except StockActivity.DoesNotExist:
            print("🆘 stock activity not found")
            raise NotFound(detail="🆘 stock activity not found")

    def get(self, _request, pk):
        stock_activity = self.get_stock_activity(pk=pk)
        serialized_stock_activity = StockActivitySerializer(stock_activity)
        return Response(serialized_stock_activity.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        stock_activity_to_edit = self.get_stock_activity(pk=pk)
        updated_stock_activity = StockActivitySerializer(stock_activity_to_edit, data=request.data)
        if updated_stock_activity.is_valid():
            updated_stock_activity.save()
            print(f"✅ stock activity ({pk}) edited")
            return Response(updated_stock_activity.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_stock_activity.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        stock_activity_to_delete = self.get_stock_activity(pk=pk)
        stock_activity_to_delete.delete()
        print("✅ stock activity ({pk}) deleted")
        return Response(status=status.HTTP_204_NO_CONTENT)