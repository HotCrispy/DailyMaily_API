from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models import CASCADE
from django.utils import timezone


class Base_Model(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다.
        """
        user = self.create_user(
            email=email,
            password=password,
            username=username,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class Model_User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        null=False,
        unique=True,
    )
    username = models.CharField(
        verbose_name='User name',
        max_length=30,
        null=True
    )
    is_active = models.BooleanField(
        verbose_name='Is active',
        default=True
    )
    date_joined = models.DateTimeField(
        verbose_name='Date joined',
        default=timezone.now
    )
    is_superuser = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = UserManager()

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = '-date_joined',


class Model_Press_Company(Base_Model):
    com_name = models.CharField(max_length=255)


class Model_News(Base_Model):
    com_id = models.OneToOneField(to=Model_Press_Company, primary_key=True, on_delete=CASCADE)
    news_title = models.CharField(max_length=255)
    news_link = models.CharField(max_length=255)
