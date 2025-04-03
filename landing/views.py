from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EarlyAccessRegistration

# Create your views here.

def home(request):
    return render(request, 'landing/home.html')

def register(request):
    if request.method == 'POST':
        EarlyAccessRegistration.objects.create(
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            phone_number=request.POST['phone_number'],
            specialization=request.POST['specialization'],
            organization=request.POST.get('organization', ''),
            want_early_access=request.POST.get('want_early_access') == 'on',
            questions=request.POST.get('questions', '')
        )
        messages.success(request, 'Thank you for your interest in KaiCure! We will notify you when early access becomes available.')
        return redirect('register')
    return render(request, 'landing/register.html')
