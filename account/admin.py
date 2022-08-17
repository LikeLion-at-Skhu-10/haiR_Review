from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from account.models import User

# Register your models here.

#관리자 화면에서 보여질 내용
class AccountAdmin(UserAdmin) : 
    
    list_display = ('username', 'name', 'email')
    search_fields = ('username', 'name', 'email') 
    

    filter_horizontal = () 
    list_filter = () 
    fieldsets = () 

#admin site 호출 
admin.site.register(User, AccountAdmin)