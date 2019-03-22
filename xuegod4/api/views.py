from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from api.models import BascUser


def test(request):
    # return HttpResponse('大家好我是for')
    return render(request,'test.html')
def register(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        isUsername = BascUser.objects.filter(username = username)
        if len(isUsername) > 0:
            return JsonResponse({'status':'400','message':'failed','data':'用户已经存在'})
        else:
            createUser = BascUser.objects.create(
                username=username,
                password=password
            ).save()
            return JsonResponse({'status':'200','message':'success','data':'用户创建成功'})


    return render(request,'index.html')