from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    pass
    

    class Meta:
        verbose_name = _("پروفایل")
        verbose_name_plural = _("پروفایل ها")

    def __str__(self):
        return 'test'

    # def get_absolute_url(self):
    #     return reverse("Profile_detail", kwargs={"pk": self.pk})
