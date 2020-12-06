# Generated by Django 3.1.3 on 2020-12-05 12:23

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
            name='makerprofile',
            fields=[
                ('maker_id', models.AutoField(primary_key=True, serialize=False)),
                ('maker_name', models.CharField(max_length=20)),
                ('maker_email', models.CharField(max_length=20)),
                ('maker_address', models.CharField(max_length=50)),
                ('maker_about', models.CharField(max_length=200)),
                ('maker_phone', models.CharField(max_length=11)),
                ('userr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]