from django.db import models

class Permission(models.Model):
    jobs = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.jobs
class Role(models.Model):
    name = models.CharField(max_length=50,unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)
    def __str__(self):
        return self.role_name
class RolePermission(models.Model):
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('role','permission')
    def __str__(self):
        return f"{self.role} -> {self.permission}"
