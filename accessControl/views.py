from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from accessControl.decorators import require_permission
from .models import Permission, Role


@login_required
@require_permission('create_permission')
def create_permission(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if Permission.objects.filter(jobs=name).exists():
            messages.error(request,"The Permission already exist!")
        else:
            Permission.objects.create(jobs=name)
            messages.success(request,"The permission is created!")
    return render(request,"accessControls/create-permission.html")

@login_required
@require_permission('create_role')
def create_role(request):
    permissions = Permission.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        permissions_ids = request.POST.getlist('permissions')

        if Role.objects.filter(name=name).exists():
            messages.error(request,"The role is already exist!")
        else:
            role = Role.objects.create(name=name)
            role.permissions.set(permissions_ids)
            messages.success(request,"The role is created and the permissions has been assigned successfully!")
    return render(request,"accessControls/create_role.html",{"permissions":permissions})
    