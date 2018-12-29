from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
# Create your views here.
from api.models import BasicUser
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        isUsername = BasicUser.objects.filter(username=username)
        if len(isUsername) > 0:
            return JsonResponse({'status':400,'message':'该用户存在'})
        else:
            createUser = BasicUser.objects.create(
                username = username,
                password = password
            )
            createUser.save()
            return JsonResponse({'status':200,'message':'用户注册成功'})
    return render(request,'index.html')

    # return JsonResponse({'a':1})