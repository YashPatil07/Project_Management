#views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()  # retrive information of client when post request call
    serializer_class = ClientSerializer
    permission_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # This custom action will handle the nested POST request for creating a project for a client
    @action(detail=True, methods=['post'], url_path='projects')
    def create_project(self, request, pk=None):
        client = self.get_object()  # Get the client object by ID (pk)
        project_name = request.data.get('project_name')
        users_data = request.data.get('users')
        
        if not project_name or not users_data:
            return Response({"error": "Project name and users are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Create the project
        project = Project.objects.create(project_name=project_name, client=client, created_by=request.user)

        # Assign users to the project
        for user_data in users_data:
            try:
                user = User.objects.get(id=user_data['id'])
                project.users.add(user)  # Add user to the project's many-to-many relationship
            except User.DoesNotExist:
                return Response({"error": f"User with id {user_data['id']} does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        project.save()

        # Serialize and return the project
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def perform_create(self, serializer):
        # Set created_by to the currently logged-in user
        serializer.save(created_by=self.request.user)
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'])
    def my_projects(self, request):
        projects = Project.objects.filter(users=request.user)
        serializer = self.get_serializer(projects, many=True)
        
        return Response(serializer.data)
    