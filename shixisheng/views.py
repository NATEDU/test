from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
import datetime

from django.template.response import TemplateResponse as TR
#from django.template import RequestContext

from shixisheng.models import student,Image
def hello(request,abc):
    #return HttpResponse('Hello Word'+ abc)
    a=datetime.datetime.now()
    d={'ab':abc,'time':str(a)}  
    all=student.objects.all()
    all_img=Image.objects.all()
    d['all_img']=all_img
    #all=student.objects.filter() 
    d['all']=all
      
    return TR(request,'index.html',d)
    #return render_to_response("wow.html",d,context_instance=RequestContext(request))

def new(request):
	print request.POST
	s= student()
	s.name=request.POST['name']
	s.address=request.POST['address']
	s.content=request.POST['content']
	s.count=0
	s.save()
	return redirect("/hello/sdfgh")

def delete(request,id):
	s=student.objects.get(id=int(id))
	s.delete()
	return redirect("/hello/sdfgh")

def edit_view(request,id):
	s=student.objects.get(id=int(id))
	t=datetime.datetime.now()
	d={"ss":s,'time':str(t)}
	return TR(request,"edit.html",d)

def edit(request,id):
	s=student.objects.get(id=int(id))
	s.name=request.POST['name']
	s.address=request.POST['address']
	s.save()
	return redirect("/hello/sdfgh")


