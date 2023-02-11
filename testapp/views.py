# from django.shortcuts import render
# from django.views.generic import View
# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from testapp.serializers import StudentSer
# from testapp.models import StudentDrf
# from django.http import HttpResponse,JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.response import Response
######
# Create your views here.
'''def student_det(request):
    stu=StudentDrf.objects.get(id=3)
    serializer=StudentSer(stu)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        no=request.POST["no"]
        name=request.POST["name"]
        address=request.POST["address"]
        phone=request.POST["phone"]
        py_data={
            'no':no, 'name':name,'address':address,'phone':phone
        }
        # data=StudentDrf(py_data)
        data1=StudentSer(data=py_data)
        print(data1)
        # data1=StudentSer(data=request.data)
        if data1.is_valid():
            print("in valid block")
            data1.save()
            return JsonResponse('data saved',safe=False)'''
########
        # json_data = request.body
        # print(request.body)
        # stream= io.BytesIO(json_data)
        # python_data=JSONParser().parse(stream)
        # serializer = StudentSer(data=python_data)
        # if serializer.is_valid():
        #     serializer.save()
        #     res = {'msg':'Data created successfully'}
        #     json_data=JSONRenderer().render(res)
        #     return HttpResponse(json_data, content_type='application/json')
        #     # return HttpResponse("Created")
        # return HttpResponse(JSONRenderer().render(serializer.errors),content_type='application/json')

'''#######################
import io
from testapp.models import StudentDrf
from testapp.serializers import StudentSer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def stu1(request):
    if request.method == 'POST':
        json_data= request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer= StudentSer(data= python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
#####################'''
#
# from testapp.models import StudentDrf
# from testapp.serializers import StudentSer
# from django.views.generic import View
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse,JsonResponse
# import io
#
# class StudentCRUD(View):
#     def get(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pydata=JSONParser().parse(stream)
#         id=pydata.get('id',3)
#         if id is not None:
#             emp=StudentDrf.objects.get(id=id)
#             serializer=StudentSer(emp)
#             json_data=JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         qs=StudentDrf.objects.all()
#         serializers=StudentSer(qs,many=True)
#         json_data=JSONRenderer().render(serializers.data)
#         return HttpResponse(json_data,content_type='application/json')
#
#     def post(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pdata=JSONRenderer

from testapp.models import StudentDrf
from testapp.serializers import StudentSer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
import io
def get_data(request):
    json_data=request.body
    stream=io.BytesIO(json_data)
    pdata= JSONParser().parse(stream)
    serializer=StudentSer(pdata)
    if serializer.is_valid():
        serializer.save()
        res={'msg':'data saved'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
    json_data=JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data,content_type='application/json')






