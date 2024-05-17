from apis.models import School
from apis.serializers import SchoolSerializer
from rest_framework import generics
from apis.filters import SchoolFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class SchoolCreateView(generics.CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    def create(self, request, *args, **kwargs):
        data = request.data
        existing_school = School.objects.filter(name=data.get('name')).first()
        if existing_school:
            return Response({"error": "School with the same name already exists."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

class SchoolListView(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter
    
class SchoolUpdateView(generics.RetrieveUpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'name'
    def get_object(self):
        name = self.kwargs.get('name')
        return get_object_or_404(School, name=name)

class SchoolDeleteView(generics.RetrieveDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'name'
    def get_object(self):
        name = self.kwargs.get('name')
        return get_object_or_404(School, name=name)
