from django.shortcuts import render, redirect
from .forms import EmailForm
from django.core.mail import send_mail

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_list = form.cleaned_data['email_list']
            subscribers = email_list.subscribers.all().values_list('email', flat=True)
            send_mail(subject, message, 'your_email@example.com', subscribers)
            return redirect('send_email')
    else:
        form = EmailForm()
    return render(request, 'send_email.html', {'form': form})
