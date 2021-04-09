from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentsSerializer
from basicserializers.models import Student

@api_view(['GET' , 'POST'])
def students_details(request):
    if request.method == 'GET':
        stu = Student.objects.all()
        serializer = StudentsSerializer(stu, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):
    if request.method == 'GET':
        stu = Student.objects.filter(id=id)
        serializer = StudentsSerializer(stu, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        stu = Student.objects.get(id=id)
        serializer = StudentsSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        stu = Student.objects.get(id=id)
        serializer = StudentsSerializer(stu)
        stu.delete()
        return Response({"msg": 'deleted'})