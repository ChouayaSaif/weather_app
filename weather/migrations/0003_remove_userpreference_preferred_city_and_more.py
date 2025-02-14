# Generated by Django 4.2.17 on 2024-12-26 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weather', '0002_alter_userpreference_preferred_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpreference',
            name='preferred_city',
        ),
        migrations.RemoveField(
            model_name='userpreference',
            name='preferred_unit',
        ),
        migrations.AddField(
            model_name='userpreference',
            name='layout',
            field=models.CharField(choices=[('grid', 'Grid'), ('list', 'List')], default='grid', max_length=100),
        ),
        migrations.AddField(
            model_name='userpreference',
            name='preferred_widgets',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='userpreference',
            name='theme',
            field=models.CharField(choices=[('light', 'Light'), ('dark', 'Dark')], default='light', max_length=100),
        ),
        migrations.AlterField(
            model_name='userpreference',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preference', to=settings.AUTH_USER_MODEL),
        ),
    ]
