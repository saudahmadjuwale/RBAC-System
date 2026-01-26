from django.http import HttpResponseForbidden
from functools import wraps

def require_permission(permission_name):
    def decorators(view_func):
        @wraps(view_func)
        def _wrapped_view(request,*args, **kwargs):
            user = request.user

            if not user.is_authenticated:
                return HttpResponseForbidden("You are not auhtenticated !")
            
            if not user.role:
                return HttpResponseForbidden("You don't have any role !")
            
            has_permission = user.role.permission.filter(name=permission_name).exist()

            if not has_permission:  
                return HttpResponseForbidden(f"You don't have permission access {permission_name} !")
            
            return view_func(request,*args,**kwargs)
        return _wrapped_view
    return decorators


