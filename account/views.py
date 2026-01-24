from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            return redirect("dashboard")
        else:
            messages.error(request,"Invalid email or password")
    return render(request,'accounts/login.html')
@login_required(login_url='login')
def dashboard(request):
    return render(request,"accounts/dashboard.html")
def logout_view(request):
    logout(request)
    return redirect("login")