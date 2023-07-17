# views.py

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render, redirect
from .models import EmailList

def send_email(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = 'your_gmail_account@gmail.com'
        email_list_ids = request.POST.getlist('email_list')  # Seçili e-posta listesi ID'leri

        email_lists = EmailList.objects.filter(id__in=email_list_ids)
        recipient_list = [email.email for email in email_lists]  # Seçili e-posta listesi kullanıcıları

        html_message = render_to_string('email_template.html', {'message': message})
        plain_message = strip_tags(html_message)

        try:
            send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)
            return redirect('admin:index')  # E-posta başarıyla gönderildiğinde yönetici paneline yönlendir
        except Exception as e:
            return render(request, 'error.html', {'error': str(e)})

    # E-posta listelerini template'e göndererek gönderme formunu oluşturun
    email_lists = EmailList.objects.all()
    return render(request, 'send_email.html', {'email_lists': email_lists})
