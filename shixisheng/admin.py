from django.contrib import admin
from .models import Student,Image,Text,Company,Partner,Href,Flow,All_Company,Login

class StudentInfoAdmin(admin.ModelAdmin):
	list_display=('id','name','company',)

class ImageInfoAdmin(admin.ModelAdmin):
	list_display=('id','name')

class TextInfoAdmin(admin.ModelAdmin):
	list_display=('id','name','info',)	

class CompanyInfoAdmin(admin.ModelAdmin):
	list_display=('id','name',)	

class PartnerInfoAdmin(admin.ModelAdmin):
	list_display=('id','name',)	

class HrefInfoAdmin(admin.ModelAdmin):
	list_display=('id','name','link',)		

class FlowInfoAdmin(admin.ModelAdmin):
	list_display=('id','title',)	

class All_CompanyInfoAdmin(admin.ModelAdmin):
	list_display=('id','name','time')	

class LoginInfoAdmin(admin.ModelAdmin):
	list_display=('id','email',)	

admin.site.register(Student,StudentInfoAdmin)
admin.site.register(Image,ImageInfoAdmin)
admin.site.register(Text,TextInfoAdmin)
admin.site.register(Company,CompanyInfoAdmin)
admin.site.register(Partner,PartnerInfoAdmin)
admin.site.register(Href,HrefInfoAdmin)
admin.site.register(Flow,FlowInfoAdmin)
admin.site.register(All_Company,All_CompanyInfoAdmin)
admin.site.register(Login,LoginInfoAdmin)
