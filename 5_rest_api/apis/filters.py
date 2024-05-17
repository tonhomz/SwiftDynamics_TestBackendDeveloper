from django_filters import FilterSet, filters
from .models import School, Student, Teacher


# code here

class SchoolFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='iexact')
    
    class Meta:
        model = School
        fields = ['name']

class TeacherFilter(FilterSet):
    firstname = filters.CharFilter(lookup_expr='iexact')
    lastname = filters.CharFilter(lookup_expr='iexact')
    gender = filters.CharFilter(lookup_expr='iexact')
    
    class Meta:
        model = Teacher
        fields = ['firstname', 'lastname', 'gender']

class StudentFilter(FilterSet):
    firstname = filters.CharFilter(lookup_expr='iexact')
    lastname = filters.CharFilter(lookup_expr='iexact')
    gender = filters.CharFilter(lookup_expr='iexact')
    
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'gender']
