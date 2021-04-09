from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StudentsSerializer
from basicserializers.models import Student
from rest_framework.response import Response

class Students_Details(APIView):
    def get(self, request):
        stu = Student.objects.all()
        serializer = StudentsSerializer(stu ,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class Student_Detail(APIView):
    def get_student(self,id):
        return Student.objects.get(id = id)

    def get(self, request, id):
        stu = self.get_student(id)
        serializer = StudentsSerializer(stu)
        return Response(serializer.data)

    def put(self, request,id):
        serializer = StudentsSerializer(self.get_student(id), data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def delete(self, request, id):
        stu = self.get_student(id)
        stu.delete()
        return Response({'msg' : 'deleted'})