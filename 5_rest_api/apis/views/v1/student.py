from apis.models import Student
from apis.serializers import StudentSerializer
from rest_framework import generics
from apis.filters import StudentFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter
    
class StudentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'firstname'
    def get_object(self):
        firstname = self.kwargs.get('firstname')
        return get_object_or_404(Student, firstname=firstname)

class StudentDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'firstname'
    def get_object(self):
        firstname = self.kwargs.get('firstname')
        return get_object_or_404(Student, firstname=firstname)
