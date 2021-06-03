from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.exceptions import NotFound
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.

from .models import StockLink
from .serializers.common import StockLinkSerializer

class StockLinkListView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, _request):
        stock_links = StockLink.objects.all()
        serialized_stock_links = StockLinkSerializer(stock_links, many=True)
        print("✅ all stock links found")
        return Response(serialized_stock_links.data, status=status.HTTP_200_OK)

    
    def post(self, request):
        stock_link_to_add = StockLinkSerializer(data=request.data)
        if stock_link_to_add.is_valid():
            stock_link_to_add.save()
            print("✅ stock link added")
            return Response(stock_link_to_add.data, status=status.HTTP_201_CREATED)
        return Response(stock_link_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class StockLinkDetailView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_stock_link(self, pk):
        try:
            print(f"✅ stock link ({pk}) found")
            return StockLink.objects.get(pk=pk)
        except StockLink.DoesNotExist:
            print("🆘 stock link not found")
            raise NotFound(detail="🆘 stock link not found")

    def get(self, _request, pk):
        stock_link = self.get_stock_link(pk=pk)
        serialized_stock_link = StockLinkSerializer(stock_link)
        return Response(serialized_stock_link.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        stock_link_to_edit = self.get_stock_link(pk=pk)
        updated_stock_link = StockLinkSerializer(stock_link_to_edit, data=request.data)
        if updated_stock_link.is_valid():
            updated_stock_link.save()
            print(f"✅ stock link ({pk}) edited")
            return Response(updated_stock_link.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_stock_link.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        stock_link_to_delete = self.get_stock_link(pk=pk)
        stock_link_to_delete.delete()
        print("✅ stock link ({pk}) deleted")
        return Response(status=status.HTTP_204_NO_CONTENT)