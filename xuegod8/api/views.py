from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
# Create your views here.
from api.models import BasicUser


def register(request):

    return render(request,'index.html')