from .models  import *
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from . forms import  *
from django.http import JsonResponse
from django.conf import settings




def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['subject']
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\n\nMessage:\n{form.cleaned_data['message']}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_RECEIVER]
            send_mail(subject, message, email_from, recipient_list)
            return JsonResponse({'success': True})
        return JsonResponse({'success': False})
    else:
        form = ContactForm()
    return render(request, 'app/index.html', {'form': form})







