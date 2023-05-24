# Generated by Django 4.2.1 on 2023-05-23 06:24

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
            name='Startups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, default=None, upload_to='image/')),
                ('Backgroundimage', models.ImageField(blank=True, default=None, upload_to='image/')),
                ('Status', models.CharField(default=None, max_length=400)),
                ('Name', models.CharField(default=None, max_length=400)),
                ('location', models.CharField(default=None, max_length=400)),
                ('Company_Type', models.CharField(default=None, max_length=400)),
                ('Company_rank', models.CharField(default=None, max_length=400)),
                ('Website', models.CharField(default=None, max_length=400)),
                ('about', models.TextField(blank=True, default=None)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
