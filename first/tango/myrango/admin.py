from django.contrib import admin
from myrango.models import Category, Page

#admin.site.register(Category)
#admin.site.register(Page)
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page,PageAdmin)
