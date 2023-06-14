from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class Login(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        Crea y guarda un usuario con el nombre de usuario y contraseña especificados.
        """
        if not username:
            raise ValueError("El nombre de usuario debe ser proporcionado.")
       
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Crea y guarda un superusuario con el nombre de usuario y contraseña especificados.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
       
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    # Aquí puedes agregar otros campos personalizados según tus requerimientos

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = Login()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
