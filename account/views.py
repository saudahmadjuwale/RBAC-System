from django.shortcuts import redirect,render, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from accessControl.decorators import require_permission
from accessControl.models import  Role

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
    users = User.objects.all()
    roles = Role.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        if not role:
            messages.error(request,"you should select a role")
        elif User.objects.filter(email=email).exists():
            messages.error(request,"The email already exist!")
        else:
            User.objects.create_user(email=email,password=password,role_id=role)
            messages.success(request,"User has been created!")
            return redirect('dashboard')
    return render(request,"accounts/create_user.html",{"roles":roles,"users":users})
@require_permission('update_role')
def update_user(request,user_id):
    user = get_object_or_404(User,id=user_id)
    roles = Role.objects.all()
    print(user)
    if request.method == "POST":
        email = request.POST.get('email')
        role_id = request.POST.get('role')
        if email and user.email != email:
            if User.objects.filter(email=email).exclude(id=user.id).exists():
                messages.error(request,"This email is already exists!")
            else:
                user.email = email
        if role_id:
            user.role_id = role_id
        user.save()
        messages.success(request,"Successfully Update!")
    return render(request,"accounts/update_user.html",{"roles":roles,'user':user})