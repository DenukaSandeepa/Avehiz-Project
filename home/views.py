from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from publishing.models import publishing

def index(request):
    publish = publishing.objects.order_by('-pub_date')

    return render(request, 'index.html',{'publish': publish })

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        #send Email
        send_mail(
           subject,#Subject
           message+ ' from '+email,#message
           email,#from
           ['denukasandeepa@gmail.com'],#to
        )

        return render(request,'contact.html',{ 'name' :  name })
    else:
        return render(request,'contact.html')
