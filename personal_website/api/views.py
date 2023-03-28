from rest_framework import generics
from .models import About, CV, Project
from .serializers import AboutSerializer, CVSerializer, ProjectSerializer

class AboutList(generics.ListCreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class CVList(generics.ListCreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer

class CVDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
