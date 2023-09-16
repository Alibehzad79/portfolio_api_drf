# Generated by Django 4.2.5 on 2023-09-15 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('date_sent', models.DateTimeField(verbose_name='تاریخ ارسال')),
            ],
            options={
                'verbose_name': 'ایمیل',
                'verbose_name_plural': 'ایمیل ها',
                'ordering': ['-date_sent'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('about_me', models.TextField(verbose_name='درباره من')),
                ('work_experience', models.IntegerField(help_text='سال', verbose_name='سابقه کار')),
                ('client_served', models.IntegerField(verbose_name='تعداد مشتری')),
                ('why_me', models.TextField(help_text='علت انتخاب من برای پروژه', verbose_name='چرا من؟')),
                ('porject_compelet', models.IntegerField(verbose_name='تعداد پروژه های انجام شده')),
                ('phone_number', models.CharField(max_length=15, verbose_name='شماره تلفن')),
                ('logo', models.ImageField(upload_to='images/logo/', verbose_name='لوگو')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'پروفایل',
                'verbose_name_plural': 'پروفایل ها',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='e.g: instagram', max_length=100, verbose_name='نام')),
                ('url', models.URLField(help_text='e.g: https://...', verbose_name='لینک')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socials', to='account_app.profile', verbose_name='Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to='images/services/', verbose_name='عکس')),
                ('url', models.URLField(blank=True, null=True, verbose_name='لینک')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serices', to='account_app.profile', verbose_name='Profile')),
            ],
        ),
        migrations.CreateModel(
            name='MyWorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='مکان')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myworkexperience', to='account_app.profile', verbose_name='Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerFeadback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام مشتری')),
                ('job', models.CharField(max_length=50, verbose_name='شغل مشتری')),
                ('feadback', models.TextField(verbose_name='توضیحات')),
                ('start', models.IntegerField(max_length=5, verbose_name='تعداد ستاره')),
                ('image', models.ImageField(upload_to='images/customers/', verbose_name='عکس مشتری')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customerfeadback', to='account_app.profile', verbose_name='Profile')),
            ],
        ),
    ]
