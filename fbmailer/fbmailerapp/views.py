from django.shortcuts import render,redirect,HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail

# Create your views here.

mymail='mail'

def code(request):
    if 'pin' in request.POST:
        if request.POST['pin'] == '0011' :
            request.session['user'] ='0011'
            return redirect('/mailer/')
        else:
            return render(request, 'mailer/code.html',{'info':'wrong pin'})
    return render(request, 'mailer/code.html')

def msg(request):
    if 'user' in request.session:
        if 'mail' in request.POST:
            htm_msg = render_to_string(request, 'mailer/fbi.html', {'sub':request.POST['sub'],'msg':request.POST['msg'],'mail':request.POST['mail']})
            send_mail(
                subject=request.POST['sub'],
                message='',
                from_email=mymail,
                recipient_list=[ request.POST['mail'] ],
                html_message=htm_msg,
                fail_silently=True

            )

            return HttpResponse('<h1 style="margin:4ex;">MESSAGE SENT!!</h1>')

        return render(request, 'mailer/sender.html')
    else:
        return redirect('/')
