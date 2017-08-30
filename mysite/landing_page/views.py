from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from landing_page.models import *
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    context = {}
    return render(request, 'landing_page/index.html', context)
# Create your views here.



def send_information(request):
	name = request.POST['name']
	email = request.POST['email']
	subject = request.POST['subject']
	message = request.POST['comment']
	

	Form_Feedback(name = name, email=email, subject=subject, message=message).save()

	from_email = settings.EMAIL_HOST_USER
	to_email = [from_email, email]

	contact_message = "%s: %s via %s" %(
		name,
	 	email,
	 	message)
	
	send_mail(
		subject,
		contact_message,
		from_email,
		to_email,
		fail_silently=False
		)

	return HttpResponseRedirect('/')
