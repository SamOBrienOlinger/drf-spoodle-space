# Generated by Django 3.2.4 on 2023-04-08 10:43

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
            name='DogProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dog_name', models.CharField(blank=True, max_length=255)),
                ('dog_age', models.IntegerField(default=0)),
                ('dog_color', models.CharField(blank=True, max_length=255)),
                ('dog_bio', models.TextField(blank=True)),
                ('dog_image', models.ImageField(default='../default_dog-profile_gtehul.png', upload_to='images/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
