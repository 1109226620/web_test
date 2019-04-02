from django.shortcuts import render,redirect
from django.http import HttpResponse
# import fasttext as ft
# import jieba
# from ..venv import classification
import classification
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# def fenci2(request):
#     txt = request.POST['txt']
#     dd = main(txt)
#     content = {'data': dd}
#     return render(request, '../templates/result.html', content)
def index(request):
    return render(request,'../templates/index.html')
def fenlei(request):
    txt = request.POST['txt']
    print(txt)
    lst = txt.split("\n")
    # res = classification.classifi(lst)
    # dic = {"result":res}
    dic = {"result": lst}
    # print(result)
    return render(request, '../templates/result.html',context=dic)