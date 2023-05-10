from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from DJANGO_EMP.dao_emp import DaoEmp

def emp_list(request):
    dao = DaoEmp()
    list = dao.selectList()
    return render(request, 'emp_list.html',{'list' : list})

def emp_detail(request):
    e_id = request.GET.get('e_id')
    dao = DaoEmp()
    detail = dao.selectOne(e_id)
    return render(request, 'emp_detail.html',{'detail' : detail})

def emp_mod(request):
    e_id = request.GET.get('e_id')
    dao = DaoEmp()
    vo = dao.selectOne(e_id)
    return render(request, 'emp_mod.html',{'vo' : vo})

@csrf_exempt
def emp_mod_act(request):
    e_id = request.POST['e_id']
    e_name = request.POST['e_name']
    sex = request.POST['sex']
    addr = request.POST['addr']
    dao = DaoEmp()
    res = dao.update(e_id, e_name, sex, addr)
    return render(request, 'emp_mod_act.html',{'res' : res})

def emp_add(request):
    return render(request, 'emp_add.html')

@csrf_exempt
def emp_add_act(request):
    e_id = request.POST['e_id']
    e_name = request.POST['e_name']
    sex = request.POST['sex']
    addr = request.POST['addr']
    dao = DaoEmp()
    res = dao.insert(e_id, e_name, sex, addr)
    return render(request, 'emp_add_act.html',{'res' : res})

@csrf_exempt
def emp_del_act(request):
    e_id = request.POST['e_id']
    dao = DaoEmp()
    res = dao.delete(e_id);
    return render(request, 'emp_del_act.html',{'res' : res})
