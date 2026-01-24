from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    role = models.ForeignKey("accessControl.Role",on_delete=models.SET_NULL,null=True,blank=True)
    USERNAME_FIELD = "email"
    
    def __str_(self):
        return self.email