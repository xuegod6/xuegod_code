from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from api.models import BasicUser
from django.http.response import JsonResponse


def register(request):
    if request.method == 'POST':
        data = request.POST
        try:
            username = data.get('username')
            password = data.get('password')
            isUsername =BasicUser.objects.filter(username=username)
        except:
            pass
        else:
            if len(isUsername
                   ) > 0:
                return JsonResponse({'status':400})
            else:
                createUser = BasicUser.objects.create(username=username,password=password)
                createUser.save()
                return JsonResponse({'status':200})
    return render(request,'index.html')