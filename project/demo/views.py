from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('demo:success')  # Redirect to the success page using the app namespace
    else:
        form = FeedbackForm()
    
    return render(request, 'index.html', {'form': form})

def success_view(request):
    return render(request,'success.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Keeping default username and password
        if username == 'admin' and password == 'admin123':
            return redirect('demo:admin_dashboard')
        else:
            return render(request, 'login.html', {'message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')
    
    
def admin_dashboard(request):
    # Retrieve form entries from the database
    form_entries = Feedback.objects.all() 
    return render(request, 'admin_dashboard.html', {'form_entries': form_entries})