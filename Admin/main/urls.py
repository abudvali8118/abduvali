from django.urls import path
from .views import *
urlpatterns=[
    path('',Index),
    path('savol/',Test),
    path('addsavol/',AddSavol),
    path('register/',Registration),
    path('login/',LoginView.as_view()),
    path('logout/',Logout),
    path('jadval/',Jadvallar),
    path("addjadval/",AddJadval),
    path('baholar/',Baholash),
    path('delete/<int:pk>/',Delete),
    path('allsavol/',SavolHammasi)
]