from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import uuid


def sendmail(request):
    link = uuid.uuid4()
    print link
    content = useTemplate('www.confirme.mail.com/'+str(link))
    try:
        subject = 'Confirme su direccion de correo electronico'
        text_content = 'habilita el html de tu correo'
        html_content = content
        from_email = '"Sophia Project" <sophiaproject4@gmail.com>'
        to = "javierperezferrada@gmail.com"
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except Exception as e:
        print "fallo sendmail"
        print e
    return JsonResponse({"response":"ok"})

def useTemplate(link):
    htmlFile = open("mailConfirmation.html")
    content = htmlFile.read()
    content = content.replace("$$link$$",str(link))
    return(content)
