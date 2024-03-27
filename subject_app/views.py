from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubjectSerializer, Subject

# Create your views here.
class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        ser_subjects = SubjectSerializer(subjects, many = True)
        return Response(ser_subjects.data)