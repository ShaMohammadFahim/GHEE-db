from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True) 

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True) 
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True) 
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username   



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
   
    print("\n" + "="*50)
    print(f"PASSWORD RESET TOKEN: {reset_password_token.key}")
    print("="*50 + "\n")

    
    send_mail(
        "Password Reset for Ghee Ecommerce",
        f"Apnar reset token holo: {reset_password_token.key}",
        "BoroVhai@ghee.com",
        [reset_password_token.user.email]
    )