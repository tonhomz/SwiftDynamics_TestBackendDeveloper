from apis.models import Teacher
from apis.serializers import TeacherSerializer
from rest_framework import generics
from apis.filters import TeacherFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class TeacherCreateView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter
    
class TeacherUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'firstname'
    def get_object(self):
        firstname = self.kwargs.get('firstname')
        return get_object_or_404(Teacher, firstname=firstname)

class TeacherDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'firstname'
    def get_object(self):
        firstname = self.kwargs.get('firstname')
        return get_object_or_404(Teacher, firstname=firstname)
    