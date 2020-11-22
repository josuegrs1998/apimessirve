from django.urls import path
from .views import RegisterView, LoginView, UserCreate, ListaUsuario, DetalleUsuario


urlpatterns =[
    path('registrar', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('usuario/create', UserCreate.as_view()),
    path('usuario', ListaUsuario.as_view()),
    path('usuario', DetalleUsuario.as_view())
]