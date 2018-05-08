from django.conf.urls import url
from django.contrib.auth.views import login as authLogin
from django.contrib.auth.views import logout

urlpatterns = [
 	url(r'^/$', 'simplemooc.accounts.views.dashboard', name='dashboard'),
    url(r'^entrar/$', authLogin, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'home'}, name='logout'),
 	url(r'^cadastre-se/$', 'simplemooc.accounts.views.register', name='register'),
 	url(r'^editar/$', 'simplemooc.accounts.views.edit', name='edit'),
 
]