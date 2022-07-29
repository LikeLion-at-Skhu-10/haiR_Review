from django.contrib import admin
from .models import Blog, p_comment, Hashtag
# Register your models here.
admin.site.register(Blog)
admin.site.register(p_comment)
admin.site.register(Hashtag)