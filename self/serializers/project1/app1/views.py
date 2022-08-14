from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def student_details(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    #json_data = JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    #json_data = JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer= StudentSerializer(data=python_data)
        if serializer.is_valid():
            res={'msg':'data saved'}
            serializer.save()
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        res={'msg':'error'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
