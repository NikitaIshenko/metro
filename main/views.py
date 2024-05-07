from django.shortcuts import render, redirect
from docxtpl import DocxTemplate
import datetime
from main.forms import DogovorForm
from main.models import Dogovor
import os
from django.http import HttpResponse
from django.urls import reverse
from django.core.mail import send_mail, EmailMessage

def index(request):
    
    form = DogovorForm()
    if request.method == "POST":
        form = DogovorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('main:dogovor', kwargs={'pk_dogovor': form.instance.pk}))

    context = {
        'form': form,
        'title': 'Метро'
    }

    return render(request, 'main/index.html', context)

def dogovor_work(request, pk_dogovor):
    dogovor = Dogovor.objects.get(pk=pk_dogovor)
    if request.method == "POST":
        if request.POST.get('download'):
            context = {
                'FIO': dogovor.get_FIO(),
                'phone': dogovor.phone,
                'email': dogovor.email,
                'passport': dogovor.passport
            }
            doc = DocxTemplate('docx/dogovor.docx')
            doc.render(context)
            file_name = f"generated_documents/dogovor_{datetime.datetime.now()}.docx"
            doc.save(file_name)
            if os.path.exists(file_name):
                with open(file_name, "rb") as fh:
                    response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                    response["Content-Disposition"] = "inline; filename=" + file_name
                    return response

    return render(request, 'main/dogovor.html', {'pk_dogovor': pk_dogovor})

def mail_dogovor(request, pk_dogovor):
    dogovor = Dogovor.objects.get(pk=pk_dogovor)
    if request.method == "POST":
        mail = request.POST.get('mail')
        context = {
            'FIO': dogovor.get_FIO(),
            'phone': dogovor.phone,
            'email': dogovor.email,
            'passport': dogovor.passport
        }
        doc = DocxTemplate('docx/dogovor.docx')
        doc.render(context)
        file_name = f"generated_documents/dogovor_{datetime.datetime.now()}.docx"
        doc.save(file_name)

        email = EmailMessage(
            "Договор",
            "Договор метро",
            "ishenkoNikita905@mail.ru",
            [mail],
        )

        email.attach_file(file_name)
        email.send()
        return redirect('main:index')
    return render(request, 'main/send-mail.html')