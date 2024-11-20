from django.urls import path
from matereia_app import views

urlpatterns = [
    path("",views.inicio_vista, name="Incio_vista"),
    path("registrarTrabajador/",views.registrarTrabajador,name="registrarTrabajador"),
    path("seleccionarTrabajador/<codigo>",views.seleccionarTrabajador,name="seleccionarTrabajador"),
    path("editarTrabajador/",views.editarTrabajador,name="editarTrabajador"),
    path("borrarTrabajador/<codigo>",views.borrarTrabajador,name="borrarTrabajador")

]