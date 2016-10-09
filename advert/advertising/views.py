from django.shortcuts import render
from advertising.models import *
from django.shortcuts import redirect
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
import Solution as S
import Tabulate as tab
import input_output_modul as inout
import math
import os

def main(request):
    return render(request, 'advertising/main.html', {'form_1': Function(), 'form_2': Function(), 'form_3': Function(), 'auto':auto()})

def params(request):
    print("HEY", request.POST)
    context = RequestContext(request)
    files = request.POST.getlist('file_path')
    a = request.POST.getlist('a')
    b = request.POST.getlist('b')
    c = request.POST.getlist('c')
    #print(int(a[0])+float(b[0])+int(c[0]))
    if request.POST.__contains__('auto_'):
        fo =  auto_param()
    else:
        fo = hands_param()
    
    x = [1,2,3,4,5,6,7,8,9,10]
    f = open("path.txt", 'w')
    if files[0] != '':
        f.write(files[0]+"\n")
    elif a[0]!='' and b[0]!='' and c[0]!= '':
        S = tab.tabulate_function(lambda x:x*float(a[0])+math.sin(x)*float(b[0])+float(c[0]),x)
        inout.write_function(x, S, "S_tab.txt")
        f.write("S_tab.txt"+"\n")
    else:
        return render_to_response('advertising/main.html',{'error': "Введите, пожалуйста, для каждой функции или параметры или путь", 'form_1': Function(), 'form_2': Function(), 'form_3': Function(), 'auto':auto()}, context)
 

    if files[1] != '':
        f.write(files[1]+"\n")
    elif a[1]!='' and b[1]!='' and c[1]!= '':
        p = tab.tabulate_function(lambda x:x*float(a[0])*(float(b[0])+x )+ float(c[0]),x)
        inout.write_function(x, p, "p_tab.txt")
        f.write("p_tab.txt"+"\n")
    else:
        return render_to_response('advertising/main.html',{'error': "Введите, пожалуйста, для каждой функции или параметры или путь", 'form_1': Function(), 'form_2': Function(), 'form_3': Function(), 'auto':auto()}, context)


    if files[2] != '':
        f.write(files[2]+"\n")
    elif a[2]!='' and b[2]!='' and c[2]!= '':
        z = tab.tabulate_function(lambda x:x*float(a[0])+math.cos(x)*float(b[0])+float(c[0]),x)
        inout.write_function(x, z, "z_tab.txt")
        f.write("z_tab.txt"+"\n")
    else:
        return render_to_response('advertising/main.html',{'error': "Введите, пожалуйста, для каждой функции или параметры или путь", 'form_1': Function(), 'form_2': Function(), 'form_3': Function(), 'auto':auto()}, context)
    f.close()


    return render(request,"advertising/params.html",{'form': fo, 'auto': True})

def results(request):
    files = open("path.txt", 'r').readlines()
    context = RequestContext(request)
    auto = True
    data = request.POST
    if request.POST.__contains__('beta'):
        auto = False
        form  = hands_param(data)
    else:
        form = auto_param(data)
    print("FILES", files)
    if form.is_valid():
        if auto:
            S.get_solution(True,files[1][:-1], files[0][:-1], files[2][:-1],request.POST.__getitem__('T'),  [], request.POST.__getitem__('y_0'), request.POST.__getitem__('beta_from'), request.POST.__getitem__('beta_to'))
            return render(request,"advertising/results_auto.html")
        else:
            S.get_solution(False,files[1][:-1], files[0][:-1], files[2][:-1],request.POST.__getitem__('T'),  [], request.POST.__getitem__('y_0'), request.POST.__getitem__('beta'), request.POST.__getitem__('x_0'))
            return render(request,"advertising/results_hands.html")
    else:
	    print(form.errors)
	    return render_to_response('advertising/params.html',{'form': form}, context)
	    
