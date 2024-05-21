from django.shortcuts import render,redirect
from app.models import Subscriber
from django.http import JsonResponse
from .forms import SubscriptionForm,ContactForm
from django.core.mail import send_mail
from django.conf import settings




def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if email already exists in the database
            if Subscriber.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already subscribed'}, status=400)
            else:
                form.save()
                return render(request, './components/subscribe.html')
        else:
            return render(request, './components/notSubscribe.html')

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)



def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email notification
            send_mail(
                'New Contact Us Submission',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_TO_EMAIL],
                fail_silently=False,
            )

            # Redirect to a thank you page
            return render(request, './components/thankyou.html')
    else:
        form = ContactForm()

    return render(request, './main/contact.html', {'form': form})



