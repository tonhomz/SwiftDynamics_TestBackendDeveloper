from apis.models import Classroom
from apis.serializers import ClassroomSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ClassroomCreateView(generics.CreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    def create(self, request, *args, **kwargs):
        data = request.data
        existing_classroom = Classroom.objects.filter(grade=data.get('grade'), section=data.get('section')).first()
        if existing_classroom:
            return Response({"error": "Classroom with the same grade and section already exists."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

class ClassroomListView(generics.ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
  
class ClassroomUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    lookup_field = 'id'
    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Classroom, id=id)

class ClassroomDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    lookup_field = 'id'
    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Classroom, id=id)
