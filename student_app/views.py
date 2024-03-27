from django.shortcuts import render
from .serializers import StudentAllSerializer, Student
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class All_students(APIView):
    def get(self, request):
        students = Student.objects.all()
        ser_students = StudentAllSerializer(students, many=True)
        return Response(ser_students.data)