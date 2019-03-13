import os,time
import face_recognition

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
all_image_path = []
result_list = []
def image_path(dir_name):
    path = os.listdir(dir_name)
    for i in path:
        abs_path = os.path.join(dir_name,i)
        all_image_path.append(abs_path)
    return all_image_path
def index(request):
    if request.method == 'POST':
        f1 = request.FILES.get('image')
        file_name = os.path.join(os.getcwd(),'./images/'+str(time.time())+'.png')
        with open(file_name,'wb') as f:
            for c in f1.chunks():
                f.write(c)
        all_path = image_path(r'E:\xuegod_code\face_django\know_image')
        n = 0

        while n < len(all_path):
            abm_image = face_recognition.load_image_file(all_path[n])
            unknown_image = face_recognition.load_image_file(file_name)
            abm_face_encoding = face_recognition.face_encodings(abm_image)[0]
            # print('chen_face_encoding:{}'.format(abm_face_encoding))
            try:
                unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
            except Exception as e:
                return HttpResponse(e)
            else:
                # print('unknow_face_encoding:{}'.format(unknown_face_encoding))
                known_faces = [
                    abm_face_encoding
            ]
            result = face_recognition.compare_faces(known_faces,unknown_face_encoding)
            result_list.append(str(result[0]))
            # if result:
            #     return HttpResponse('success')
            # else:
            #     return JsonResponse({'message':'错误'})
            n += 1
        print(result_list)
        # if 'True' in result_list:
        #     return HttpResponse('successful 这个人有权限')
        # else:
        #     return HttpResponse('bad 这个人没有权限')
    return render(request,'index.html')

