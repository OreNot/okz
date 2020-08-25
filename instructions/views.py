import os
from email.mime.application import MIMEApplication
from os.path import basename

from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.

# Create your views here.

from datetime import datetime
from datetime import date
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List
from okz.settings import STATIC_DIR

# here I want the /static/image.jpg file then

import time

import psycopg2

def send_mail(
        sender,
        receivers: List[str],
        subject,
        body,
        files=None
):
    creds = []
    with open('C:\Creds\creds.txt', 'r') as f:
        for str in f:
            if str not in creds:
                creds.append(str)

    login = creds[0].replace('\n', '').replace(' ', '')
    pasw = creds[1].replace('\n', '').replace(' ', '')
    """Sends an email to the specified receivers using an Exchange server."""
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = ",".join(receivers)
    message["Subject"] = subject
    message.attach(MIMEText(body))


    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        message.attach(part)

    server = smtplib.SMTP('core-s-exh01.gk.rosatom.local', 587)
    server.starttls()
    server.login(login, pasw)
    server.sendmail(sender, receivers, message.as_string())
    server.quit()


def instrictions(request):
    if (request.method == 'POST'):
            file_list=[]
            files = request.POST.getlist('checks[]')
            for file in files:
                file = os.path.join(STATIC_DIR, file)
                file_list.append(file)
            print(files)
            email = request.POST['email']
            print(email)
            send_mail('sep@rosatom.ru', email, files,
                      'Добрый день!\nВо вложении следующие файлы '+ files,
                      file_list
                      )

            return render(request, 'instructions/instructions.html')
    return render(request, 'instructions/instructions.html')