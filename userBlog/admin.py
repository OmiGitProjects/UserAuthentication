from django.contrib import admin
from .models import  MyBlogsDatabase, ContactDatabase

@admin.register(MyBlogsDatabase)
class PostAdmin(admin.ModelAdmin):
        class Media:
                js = ('userBlog/js/tinyInject.js',)

admin.site.register(ContactDatabase)