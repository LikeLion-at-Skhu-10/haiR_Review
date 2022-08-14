from re import M
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.

class UserManager(BaseUserManager) :
    def create_user (self, email, username, name, password=None,) : 
        if not username : 
            raise ValueError("아이디를 입력해주세요")
        if not email : 
            raise ValueError("이메일을 입력해주세요")
        if not name : 
            raise ValueError("닉네임을 입력해주세요")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username, #아이디 
            name = name, #닉네임
            password = password 
        )

        user.set_password(password)
        user.save(using=self.db) 
        return user

    #관리자 User 
    def create_superuser(self, email, username, name, password) :
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            name = name,
            password = password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db) 
        return user 

class User(AbstractBaseUser) :
    username = models.CharField(max_length=20, unique=True) 
    name = models.CharField (max_length=20, null=False, blank=False) 
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    p_num = models.IntegerField (null=True)
    profile_Img = models.ImageField(upload_to='images/', blank = True)
    create_at = models.DateTimeField(verbose_name='date joined', auto_now_add=True) 
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 

    objects = UserManager() 

    USERNAME_FIELD = 'username' #username ID 로 사용 
    REQUIRED_FIELDS = ['name', 'email'] #그 외에 필수로 필요한 내용

    def __str__(self) :
        return self.username 

    #권한 확인
    def has_perm(self, perm, obj=None) :
        return self.is_admin 

    #권한 확인 후 모델 접근 가능 
    def has_module_perms(self, app_label) :
        return True 

    #True 반환 시 관리자 로그인 가능 
    @property 
    def is_staff (self) : 
        return self.is_admin
            