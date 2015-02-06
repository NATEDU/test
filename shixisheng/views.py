from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
import datetime

from django.template.response import TemplateResponse as TR
#from django.template import RequestContext

from shixisheng.models import Student,Image,Text,Company,Partner,Href,Flow,All_Company,Login
def hello(request):
    c=Company.objects.all()[:8] 
    s=Student.objects.all()[:5]  
    t=Text.objects.all()[:6]
    t_all=Text.objects.all()
    p=Partner.objects.all()[:9]
    h=Href.objects.all()
    f=Flow.objects.all()
    i=Image.objects.all()
    d={'all_company':c,'student':s,'text':t,'partner':p,'href':h,'flow':f}    
    for x in t_all:	
    	d[x.name]=x.info    
    for x in i:
    	d[x.name]=x.img
    	
    return TR(request,'index.html',d)
    #return render_to_response("wow.html",d,context_instance=RequestContext(request))

def login(request):
	return TR(request,'login.html')

def all_company(request):
	ac=All_Company.objects.all()
	h=Href.objects.all()
	t=Text.objects.all()
	d={'ac':ac,'href':h}
	for x in t:
		d[x.name]=x.info
	return TR(request,'bc.html',d)

def new(request):
	l=Login()
	l.email=request.POST['email']
	l.password=request.POST['password']
	l.save()
	return redirect("/hello")

def delete(request,id):
	s=Student.objects.get(id=int(id))
	s.delete()
	return redirect("/hello/sdfgh")

def edit_view(request,id):
	s=Student.objects.get(id=int(id))
	t=datetime.datetime.now()
	d={"ss":s,'time':str(t)}
	return TR(request,"edit.html",d)

def edit(request,id):
	s=Student.objects.get(id=int(id))
	s.name=request.POST['name']
	s.address=request.POST['address']
	s.save()
	return redirect("/hello/sdfgh")


