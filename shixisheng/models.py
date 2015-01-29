#coding:utf-8
from django.db import models

class Image(models.Model):
	name=models.CharField(max_length=30)
	img=models.ImageField(upload_to='./img')	

class Text(models.Model):
	name=models.CharField(max_length=1024)
	info=models.CharField(max_length=1024)	

class Href(models.Model):
	name =	models.CharField(max_length=30)
	link=	models.CharField(max_length=30)	

class Student(models.Model):
	name	= models.CharField(max_length=30)
	company = models.CharField(max_length=50)
	img=models.ImageField(upload_to='./img')
	info 	= models.CharField(max_length=1024)
	post = models.TextField()

class Company(models.Model):
	name	= models.CharField(max_length=30)
	img=models.ImageField(upload_to='./img')
	info = models.TextField()

class Partner(models.Model):
	name = models.CharField(max_length=30)
	link = models.CharField(max_length=50)
	img  =models.ImageField(upload_to='./img')	

class Flow(models.Model):
	title = models.CharField(max_length=30)
	info = models.CharField(max_length=1024)
	img  =models.ImageField(upload_to='./img')	

class All_Company(models.Model):
	post = models.CharField(max_length=30)
	info = models.CharField(max_length=1024)
	name = models.CharField(max_length=30)
	money = models.CharField(max_length=30)
	time = models.DateTimeField(auto_now_add=True)
	
class Login(models.Model):
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=12)
	captcha = models.CharField(max_length=5)
	