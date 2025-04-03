from django.db import models

# Create your models here.

class EarlyAccessRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    specialization = models.CharField(max_length=100)
    organization = models.CharField(max_length=200, blank=True, null=True)
    want_early_access = models.BooleanField(default=True)
    questions = models.TextField(blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        ordering = ['-registration_date']
