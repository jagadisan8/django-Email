from django.shortcuts import render
from emailapp import forms
from emailproject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.



def subscribe(request):
    sub=forms.Subscribe()
    if request.method == 'POST':
        sub=forms.Subscribe(request.POST)
        subject = "infomation from jagadish"
        message = "HOPE YOU ARE DOING WELL"
        recepient = str(sub['Email'].value())
        send_mail(subject,message,
              EMAIL_HOST_USER,[recepient], fail_silently=False)
        return render(request,'emailapp/success_email.html',{'recepient':recepient})
    return render(request,'index.html',{'form':sub})
