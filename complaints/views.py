from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import ComplaintForm, UserRegisterForm
from .models import Complaint

# Check if user is admin
def is_admin(user):
    return user.is_superuser

# Redirect root to login
def home(request):
    return redirect('login')

# User registration
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # This hashes the password correctly
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def contact_view(request):
    return render(request, 'contact.html')

# Custom login
def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect after successful login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard for both users and admin
@login_required
def dashboard(request):
    if request.user.is_superuser:
        complaints = Complaint.objects.all()
    else:
        complaints = Complaint.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'complaints': complaints})

# Submit complaint
@login_required
def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            messages.success(request, "Complaint submitted successfully.")
            return redirect('dashboard')
    else:
        form = ComplaintForm()
    return render(request, 'complaint_form.html', {'form': form})

# Admin-only complaint status update
@user_passes_test(is_admin, login_url='login')
def update_status(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    if request.method == 'POST':
        complaint.status = request.POST['status']
        complaint.save()
        messages.success(request, "Status updated successfully.")
        return redirect('dashboard')
    return render(request, 'update_status.html', {'complaint': complaint})

@login_required
def delete_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)

    # Allow only owner or admin to delete
    if complaint.user != request.user and not request.user.is_superuser:
        return HttpResponseForbidden("You are not allowed to delete this complaint.")
    
    if request.method == "POST":
        complaint.delete()
        messages.success(request, "Complaint deleted successfully.")
        return redirect('dashboard')
    
    # Optionally render a confirmation page instead of direct delete
    return render(request, 'confirm_delete.html', {'complaint': complaint})