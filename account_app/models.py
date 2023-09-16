from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
# Create your models here.

class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_("User"), on_delete=models.CASCADE)
    full_name = models.CharField(_("نام و نام خانوادگی"), max_length=100)
    about_me = models.TextField(_("درباره من"))
    work_experience = models.IntegerField(_("سابقه کار"), help_text=_("سال"))
    client_served = models.IntegerField(_("تعداد مشتری"))
    why_me = models.TextField(_("چرا من؟"), help_text=_("علت انتخاب من برای پروژه"))
    porject_compelet = models.IntegerField(_("تعداد پروژه های انجام شده"))
    phone_number = models.CharField(_("شماره تلفن"), max_length=15)
    logo = models.ImageField(_("لوگو"), upload_to="images/logo/")
    
    
    class Meta:
        verbose_name = _("پروفایل")
        verbose_name_plural = _("پروفایل ها")

    def __str__(self):
        return self.full_name

class Project(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(_("عنوان"), max_length=50)
    image = models.ImageField(_("عکس"), upload_to="images/services/")
    url = models.URLField(_("لینک"), max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = _("پروژه ها")
    def __str__(self):
        return self.title
    
class Service(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE, related_name="services")
    title = models.CharField(_("عنوان"), max_length=50)
    image = models.ImageField(_("عکس"), upload_to="images/services/")
    url = models.URLField(_("لینک"), max_length=200, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = _("سرویس ها")
    def __str__(self):
        return self.title

class MyWorkExperience(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE, related_name="myworkexperience")
    place = models.CharField(_("مکان"), max_length=50)
    date = models.DateField(_("تاریخ"), auto_now=False, auto_now_add=False)
    title = models.CharField(_("عنوان"), max_length=50)
    description = models.TextField(_("توضیحات"))
    
    class Meta:
        verbose_name_plural = _("تجربیات")
    def __str__(self):
        return self.profile.full_name

class Social(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE, related_name="socials")
    name = models.CharField(_("نام"), max_length=100, help_text=_("e.g: instagram"))
    url = models.URLField(_("لینک"), max_length=200, help_text=_("e.g: https://..."))
    
    class Meta:
        verbose_name_plural = _("شبکه های اجتماعی")
    def __str__(self):
        return self.profile.full_name
    
class CustomerFeadback(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=_("Profile"), on_delete=models.CASCADE, related_name="customerfeadback") 
    name = models.CharField(_("نام مشتری"), max_length=50)
    job = models.CharField(_("شغل مشتری"), max_length=50)
    feadback = models.TextField(_("توضیحات"))
    start = models.IntegerField(_("تعداد ستاره"))
    image = models.ImageField(_("عکس مشتری"), upload_to="images/customers/")
    
    class Meta:
        verbose_name_plural = _("رضایت مشتری ها")
    def __str__(self):
        return self.profile.full_name

class Email(models.Model):
    email = models.EmailField(_("ایمیل"), max_length=254)
    date_sent = models.DateTimeField(_("تاریخ ارسال"), auto_now=False, auto_now_add=False, blank=True, null=True)
    
    class Meta:
        verbose_name = _("ایمیل")
        verbose_name_plural = _("ایمیل ها")
        ordering = [
            '-date_sent'
        ]
    def __str__(self):
        return self.email
    