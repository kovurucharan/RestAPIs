from django.shortcuts import render,get_object_or_404
from WebApp.models import Employeee
from rest_framework.views import APIView
from  django.http import HttpResponseRedirect,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer

# Create your views here.
def Home(request):
    obj=Employeee.objects.all()
    return render(request,'MyApp/home.html',{'obj':obj})

class EmpList(APIView):
    def get(self,request):
        obj=Employeee.objects.all()
        serializer=EmployeeSerializer(obj,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            std=Employeee.objects.get(id=id)
            serializer=EmployeeSerializer(std)
            return Response(serializer.data)
        std = Employeee.objects.all()
        serializer=EmployeeSerializer(std,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        id=pk
        std = Employeee.objects.get(pk=id)
        serializer = EmployeeSerializer(std,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"completly updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,pk,format=None):
        id = pk
        std = Employeee.objects.get(pk=id)
        serializer = EmployeeSerializer(std, request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "partially updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        id=pk
        std=Employeee.objects.get(pk=id)
        std.delete()
        return Response({"msg":'Deleted'})


