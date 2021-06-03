from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.exceptions import NotFound
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import ActivityDefinition
from .serializers.common import ActivityDefinitionSerializer

# Create your views here.

class ActivityDefinitionListView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, _request):
        categories = ActivityDefinition.objects.all()
        serialized_categories = ActivityDefinitionSerializer(categories, many=True)
        print("✅ all activity definitions found")
        return Response(serialized_categories.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        activity_definition_to_add = ActivityDefinitionSerializer(data=request.data)
        if activity_definition_to_add.is_valid():
            activity_definition_to_add.save()
            print("✅ activity definition created")
            return Response(activity_definition_to_add.data, status=status.HTTP_201_CREATED)
        return Response(activity_definition_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ActivityDefinitionDetailView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_activity_definition(self, pk):
        try:
            print(f"✅ activity definition ({pk}) found")
            return ActivityDefinition.objects.get(pk=pk)
        except ActivityDefinition.DoesNotExist:
            print("🆘 activity definition not found")
            raise NotFound(detail="🆘 activity definition not found")
    
    def get(self, _request, pk):
        activity_definition = self.get_activity_definition(pk=pk)
        serialized_activity_definition = ActivityDefinitionSerializer(activity_definition)
        return Response(serialized_activity_definition.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        activity_definition_to_edit = self.get_activity_definition(pk=pk)
        updated_activity_definition = ActivityDefinitionSerializer(activity_definition_to_edit, data=request.data)
        if updated_activity_definition.is_valid():
            updated_activity_definition.save()
            print(f"✅ activity definition ({pk})  edited")
            return Response(updated_activity_definition.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_activity_definition.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        activity_definition_to_delete = self.get_activity_definition(pk=pk)
        activity_definition_to_delete.delete()
        print(f"✅ activity definition ({pk}) deleted")
        return Response(status=status.HTTP_204_NO_CONTENT)