from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.exceptions import NotFound
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Category
from .serializers.common import CategorySerializer

# Create your views here.

class CategoryListView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, _request):
        categories = Category.objects.all()
        serialized_categories = CategorySerializer(categories, many=True)
        print("✅ categories found")
        return Response(serialized_categories.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        category_to_add = CategorySerializer(data=request.data)
        if category_to_add.is_valid():
            category_to_add.save()
            print("✅ category created")
            return Response(category_to_add.data, status=status.HTTP_201_CREATED)
        return Response(category_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class CategoryDetailView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_category(self, pk):
        try:
            print("✅ category found")
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            print("🆘 category not found")
            raise NotFound(detail="🆘 category not found")
    
    def get(self, _request, pk):
        category = self.get_category(pk=pk)
        serialized_category = CategorySerializer(category)
        return Response(serialized_category.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        category_to_edit = self.get_category(pk=pk)
        updated_category = CategorySerializer(category_to_edit, data=request.data)
        if updated_category.is_valid():
            updated_category.save()
            print("✅ category edited")
            return Response(updated_category.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_category.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        category_to_delete = self.get_category(pk=pk)
        category_to_delete.delete()
        print("✅ category deleted")
        return Response(status=status.HTTP_204_NO_CONTENT)