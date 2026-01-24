from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.role_name
class Permission(models.Model):
    jobs = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.jobs
class RolePermission(models.Model):
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('role','permission')
    def __str__(self):
        return f"{self.role} -> {self.permission}"
