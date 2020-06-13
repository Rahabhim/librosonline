from django.contrib import admin
from vistaprevia.models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    fields =['fecha_publicacion' , 'producto']


admin.site.register(Producto, ProductoAdmin)
