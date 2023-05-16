from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from flask import json
from DJANGO_MVVM import dao_emp
from DJANGO_MVVM.dao_emp import DaoEmp
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def ajax(request):
    param = json.loads(request.body)
    print("param",param['menu'])
    context = {
        'result' : 'ok'
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_list(request):
    dao = DaoEmp()
    list = dao.selectList();
    context = {
        'list' : list
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_detail(request):
    # e_id = request.POST['e_id']
    param = json.loads(request.body)
    e_id = param['e_id']
    dao = DaoEmp()
    data = dao.selectOne(e_id);
    context = {
        'data' : data
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_update(request):
    param = json.loads(request.body)
    e_id = param['e_id']
    e_name = param['e_name']
    sex = param['sex']
    addr = param['addr']
    print("param",param['e_id'])
    dao = DaoEmp()
    res = dao.update(e_id, e_name, sex, addr)
    context = {
        'res' : res
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_add(request):
    param = json.loads(request.body)
    e_id = param['e_id']
    e_name = param['e_name']
    sex = param['sex']
    addr = param['addr']
    dao = DaoEmp()
    res = dao.insert(e_id, e_name, sex, addr)
    context = {
        'res' : res
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_del(request):
    param = json.loads(request.body)
    e_id = param['e_id']
    dao = DaoEmp()
    res = dao.delete(e_id)
    context = {
        'res' : res
    }
    return JsonResponse(context)
   