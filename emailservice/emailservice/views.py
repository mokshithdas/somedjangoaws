from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    if request.method=='POST':
        print('IN POST')
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        data={
            'name':name,
            'email':email,
            'subject':subject,
            'message':message
        }
        print(data)
        message='''
        New Message: {}

        From: {}
        '''.format(data['message'],data['name'])
        send_mail(data['subject'],message, '' , [data['email']])
    return render(request,'emailservice/index.html',{})