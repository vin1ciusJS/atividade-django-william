from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clientes.urls')),
    path('api/', include('fornecedores.urls')),
    path('api/', include('funcionarios.urls')),
    path('api/', include('nota_fiscal.urls')),
    path('api/', include('produtos.urls')),
]