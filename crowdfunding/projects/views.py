
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializer import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
# This update tells the view that if a POST request comes through, it should load thedata into the serializer, tell the serializer to save a new record to the database, and
# then respond with the JSON detailing what was saved.

class ProjectDetail(APIView):

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:          
            raise Http404
    
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
            instance=project,
            data=request.data,
            partial=True
            )
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
            # return Response("updated thanks!") - alternative response
        return Response(serializer.errors)
    
# Notice that we haven't implemented status codes or error handling here for you. Ifyou don't remember how, take a look back at the previous content block in whichwe demonstrated that. Remember, you can ask the mentors if you get stuck!
    
class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
        
        
        
