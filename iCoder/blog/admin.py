from django.contrib import admin
from blog.models import Post, BlogComment

# Register your models here.
# admin.site.register(Post)
admin.site.register(BlogComment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('inject.js',)


# you can also give above things like this 
# admin.site.register((Post, BlogComment))