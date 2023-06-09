from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
class Productcurd(APIView):
    def get(self,request):
        PQS=Product.objects.all()
        PJD=productMS(PQS,many=True)
        return Response(PJD.data)
    def post(self,request):
        PMSD=productMS(data=request.data)
        if PMSD.is_valid():
            SPO=PMSD.save()
            return Response({'message':'product is created' })
        else:
            return Response({'failed':'product creation is failed'})
    def put(self,request):
        id=request.data['id']
        Productobject=Product.objects.get(id=id)
        PMSD=productMS(Productobject,data=request.data)
        if PMSD.is_valid():
            SPO=PMSD.save()
            return Response({'message':'product is updated' })
        else:
            return Response({'failed':'product creation is failed'})
        