from django.urls import path, include
from .views import home, json, CustomLoginView, CustomLogoutView, KomendaCreateView, KomendaDeleteView, KomendaUpdateView
urlpatterns = [
    path('', home, name="home"),
    path('json/', json),
    path('komendacreate/', KomendaCreateView.as_view(), name="komenda_create"),
    path('komendaupdate/<pk>', KomendaUpdateView.as_view(), name="komenda_update"),
    path('komendadelete/<pk>', KomendaDeleteView.as_view(), name="komenda_delete"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
]
