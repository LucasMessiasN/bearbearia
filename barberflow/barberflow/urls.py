from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('cadastro_user/', views.cadastro_user, name='cadastro_user'),
    path('lista_users/', views.lista_users, name='lista_users'),
    path('deletar_user/<int:user_id>/', views.deletar_user, name='deletar_user'),
    
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('cadastro_cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('editar_cliente/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('deletar_cliente/<int:cliente_id>/', views.deletar_cliente, name='deletar_cliente'),

    path('lista_barbeiros/', views.lista_barbeiros, name='lista_barbeiros'),
    path('cadastro_barbeiros/', views.cadastro_barbeiros, name='cadastro_barbeiros'),
    path('deletar_barbeiro/<int:barbeiro_id>/', views.deletar_barbeiro, name='deletar_barbeiro'),

    path('lista_atendimentos/', views.lista_atendimentos, name='lista_atendimentos'),
    path('cadastro_atendimento/', views.cadastro_atendimento, name='cadastro_atendimento'),
    path('concluir_atendimento/<int:atendimento_id>/', views.concluir_atendimento, name='concluir_atendimento'),

    path('historico_atendimentos/', views.historico_atendimentos, name='historico_atendimentos'),
]
