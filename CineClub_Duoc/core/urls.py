from django.urls import path
from .views import index
from .views import datos_ingresados
from .views import detalle
from .views import formulario
from .views import iniciar_sesion
from .views import posts
from django.conf import settings
from django.conf.urls.static import static


urlpatterns= [
    path('', index,name="index"),
    path('', datos_ingresados,name="datos_ingresados"),
    path('', detalle,name="detalle"),
    path('', formulario,name="formulario"),
    path('', iniciar_sesion,name="iniciar_sesion"),
    path('', posts,name="posts"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)