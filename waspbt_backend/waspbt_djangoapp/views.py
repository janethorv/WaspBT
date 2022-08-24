from django.shortcuts import render
from .serializers import ProjectSerializer, IssueSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
