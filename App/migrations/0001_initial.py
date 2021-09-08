# Generated by Django 3.2.7 on 2021-09-06 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('cName', models.CharField(max_length=50, primary_key='true', serialize=False, unique='true')),
                ('cEmail', models.EmailField(max_length=254)),
                ('cLogo', models.ImageField(blank=True, upload_to='images')),
                ('cUrl', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eFname', models.CharField(max_length=50, primary_key='true', serialize=False, unique='true')),
                ('eLname', models.CharField(max_length=50)),
                ('eEmail', models.EmailField(max_length=254)),
                ('ePhone', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('eCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.company')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]