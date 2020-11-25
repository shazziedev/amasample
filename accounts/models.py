from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver	
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


from django.utils import timezone
import random , os , requests


from .manager import Usermanager


class User(AbstractBaseUser, PermissionsMixin):
	avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
	phone_regex 	= RegexValidator(
		regex 		= r'^\+?1?\d{9,14}$',
		message		= 'phone number must be in the format: +260xxxxxxxxx',
		)
	phone 			= models.CharField(validators = [phone_regex], max_length=15 , unique = True )
	first_name      = models.CharField(max_length=150 ,default=None, null=True,blank=True)
	last_name       = models.CharField(max_length=150,default=None, null=True,blank=True)
	dob				= models.DateField(blank=True, null=True)
	is_staff        = models.BooleanField(default=False)
	is_active       = models.BooleanField(default=True)
	first_login		= models.BooleanField(default=False)
	date_joined     = models.DateTimeField(default=timezone.now)
	last_login      = models.DateTimeField(null=True)

	objects = Usermanager()

	USERNAME_FIELD 	= 'phone'

	REQUIRED_FIELDS = []

	def get_full_name(self):
		return self.first_name






