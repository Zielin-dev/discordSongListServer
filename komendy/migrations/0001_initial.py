# Generated by Django 4.0.3 on 2022-06-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Komenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('command', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('volume', models.IntegerField(default=1)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]