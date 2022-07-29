from django.contrib import admin
from .models import Blog, r_comment, Hashtag
# Register your models here.
admin.site.register(Blog)
admin.site.register(r_comment)
admin.site.register(Hashtag)



