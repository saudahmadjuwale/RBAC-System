from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from accessControl.decorators import require_permission
from .models import Permission

@login_required
@user_passes_test(lambda u: u.is_staff)
def create_permission(request):
    if request.method == "POST":
        name = request.POST.get('name')

        if Permission.objects.filter(jobs=name).exists():
            messages.error(request,"The Permission already exist!")
        else:
            Permission.objects.create(jobs=name)
            messages.success(request,"The permission is created!")
    return render(request,"accessControls/create-permission.html")