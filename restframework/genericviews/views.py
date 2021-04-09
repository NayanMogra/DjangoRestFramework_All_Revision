from django.shortcuts import render
from basicserializers.models import Student
from .serializers import StudentsSerializer
from rest_framework import generics
from rest_framework import mixins

class Students_Details(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = StudentsSerializer
    queryset = Student.objects.all()
    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request, id)
        return self.list(request)

    def post(self,request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request,id)

    def delete(self,request , id = None):
        return self.destory(request,id)