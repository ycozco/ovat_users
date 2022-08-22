from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager para perfiles de usuario personalizados"""

    def create_user(self, email, name, password=None):
        """Crea y guarda un nuevo usuario"""

        if not email:
            raise ValueError('El email debe ser obligatorio')
        """" correo a lower case"""
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Crea y guarda un nuevo superusuario"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractUser, PermissionsMixin):
    """ modelo base de datos para usuarios"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Devuelve el nombre completo del usuario"""
        return self.name
    def get_short_name(self):
        """ Devuelve el nombre del usuario"""
        return self.name
    
    def __str__(self):
        """ Devuelve una representacion en cadena del objeto"""
        return self.email



""" CliNom	Cliente nombre
CliEma	Cliente email
CliPas	cliente contrasena
CliNumTel	Cliente numero de telefono
CliTipDoc	Cliente tipo de documento
CliNumDoc	Cliente numero de documento
CliFecCum	Cliente fecha de cumpleanos
CliHueDig	Cliente huella digital
CliMemCod	Cliente Membresia codigo
CliMemIni	Cliente Membresia inicio
CliMemFin	Cliente Membresia Fin """
