from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.exceptions import NotFound
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Name
from .serializers.common import NameSerializer

# Create your views here.

class NameListView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, _request):
        names = Name.objects.all()
        serialized_names = NameSerializer(names, many=True)
        print("✅ names found")
        return Response(serialized_names.data, status=status.HTTP_200_OK)

    def post(self, request):
        name_to_add =  NameSerializer(data=request.data)
        if name_to_add.is_valid():
            name_to_add.save()
            print("✅ name created")
            return Response (name_to_add.data, status=status.HTTP_201_CREATED)
        return Response(name_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class NameDetailView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_name(self, pk):
        try:
            print("✅ name found")
            return Name.objects.get(pk=pk)
        except Name.DoesNotExist:
            print("🆘 name not found")
            raise NotFound(detail="🆘 name not found")
    
    def get(self, _request, pk):
        name = self.get_name(pk=pk)
        serialized_name = NameSerializer(name)
        return Response(serialized_name.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        name_to_edit = self.get_name(pk=pk)
        updated_name = NameSerializer(name_to_edit, data=request.data)
        if updated_name.is_valid():
            updated_name.save()
            print("✅ name edited")
            return Response(updated_name.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_name.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        name_to_delete = self.get_name(pk=pk)
        name_to_delete.delete()
        print("✅ name deleted")
        return Response(status=status.HTTP_204_NO_CONTENT)
