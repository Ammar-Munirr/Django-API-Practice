from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serialer = StudentSerializer(data=python_data)
        if serialer.is_valid():
            serialer.save()
            print('Data Created')
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id= python_data.get('id',None)
        if id is not None:
            item = Student.objects.get(id=python_data['id'])
            serialer = StudentSerializer(item)
            return JsonResponse(serialer.data,safe=False)
        item = Student.objects.all()
        serialer = StudentSerializer(item,many = True)
        return JsonResponse(serialer.data,safe=False)