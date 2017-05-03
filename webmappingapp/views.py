# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import points
from .serializers import pointsSerializer

# Create your views here.
class pointsList(APIView):
    def get(self,request):
        point = points.objects.all()
        serializer = pointsSerializer(point, many=True)
        return Response(serializer.data)

    def post(self):
        pass