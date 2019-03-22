from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def getpage(request):

    return render(request,'getpage.html')

def sendpage(request):
    userList = ["while","miss","for","mk","cd","other"] #用户池
    result = {"state": "error","data": ""} #返回结果的数据结构
    if request.method == "GET" and request.GET:
        request_name = request.GET.get("username")
        if request_name:
            if request_name in userList:
                result["data"] = "用户名重复"
            else:
                result["state"] = "success"
                result["data"] = "没有问题，可以注册"
        else:
            result["data"] = "请输入用户名"
    else:
        result["state"] = "error"
        result["data"] = "我们只接受get请求"
    return JsonResponse(result)
