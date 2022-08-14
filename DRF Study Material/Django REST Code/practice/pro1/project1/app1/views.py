from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from django.http import HttpResponse,JsonResponse
# Create your views here.

def Student_info(request):
    stu=Student.objects.all()
    serializer= StudentSerializer(stu)
    return JsonResponse(serializer.data)

    
