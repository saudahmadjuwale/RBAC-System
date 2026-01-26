from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from accessControl.decorators import require_permission
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
User = get_user_model()
@require_permission('create_user')
def create_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            messages.error(request,"The email already exist!")
        else:
            User.objects.create_user(email=email,password=password)
            messages.success(request,"User has been created!")
            return redirect('dashboard')
    return render(request,"accounts/create_user.html")