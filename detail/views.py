from django.shortcuts import render
from django.http import HttpResponse
from .models import student
import MySQLdb

def renderPage(req):
    return render(req,"home.html")

def saveData(req):

    obj=student()
    obj.id=req.GET.get('id')
    obj.s_name=req.GET.get('name')
    obj.s_age=req.GET.get('age')
    obj.s_mobile=req.GET.get('mobile')
    obj.s_address=req.GET.get('address')
    obj.s_marks=req.GET.get('marks')
    obj.save()
    return HttpResponse("savedata")
    
def viewall(req):
    record=student.objects.all()
    return render(req,"viewALLrecord.html",{'A':record})

def searchdata(req):
    id=req.GET.get('id')
    record=student.objects.get(id=id)
    return render(req,"edit.html",{'record':record})

def update(req):
    obj=student()
    obj.id=req.GET.get('id')
    obj.s_name=req.GET.get('name')
    obj.s_age=req.GET.get('age')
    obj.s_mobile=req.GET.get('mobile')
    obj.s_address=req.GET.get('address')
    obj.s_marks=req.GET.get('marks')
    obj.save()
    return HttpResponse("update")

def deletedata(req):
    id=req.GET.get('id')
    record=student.objects.get(id=id)
    record.delete()
    return HttpResponse("delete")