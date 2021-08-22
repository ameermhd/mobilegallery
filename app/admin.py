from django.contrib import admin
from.models import *

class catadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields ={'slug':('name',)}
admin.site.register(categ,catadmin)


class proadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available']
    list_editable = ['price','stock']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,proadmin)



