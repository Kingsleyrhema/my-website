from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404
from .models import Expert, Document
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
import os

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

def download_cv(request):
    position = request.GET.get('position')
    if position:
        try:
            expert = Expert.objects.get(position__icontains=position)
            document = expert.document  # Access the related document
            file_path = document.resume.path
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/force-download")
                    response['Content-Disposition'] = f'inline; filename={os.path.basename(file_path)}'
                    return response
            else:
                raise Http404
        except Expert.DoesNotExist:
            raise Http404("No expert found with that position.")
    raise Http404("Invalid request.")
