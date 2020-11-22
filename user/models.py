from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from .managers import CustomUserManager

#Here you add the models for the user, in case we are having different models based on clients
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True, error_messages={
        'unique': "Cuenta con esta direccion de E-Mail ya existe!"
    })
    telefono = models.CharField(null=True, max_length=20)
    direccion = models.JSONField(null=True)
    #activate = models.JSONField(null=True)
    #reset_expiration = models.DateTimeField(null=True)
#    is_active = models.BooleanField(
 #       _('active'),
  #      default=False,
   #     help_text=_(
    #        'Designates whether this user should be treated as active. '
     #       'Unselect this instead of deleting accounts.'
      #  ),
    #)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    #This is the call to the custom manager to add more manage the user model
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    class Meta:
        db_table = "auth_user"