from django.urls import path, include

import main.views as main

app_name = 'main'

urlpatterns = [
    path("", main.index, name="index"),
    path("dogovor/<int:pk_dogovor>/", main.dogovor_work, name="dogovor"),
    path("send-mail/<int:pk_dogovor>/", main.mail_dogovor, name="send_mail")
]