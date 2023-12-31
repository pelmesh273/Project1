# Generated by Django 3.2 on 2023-11-16 18:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Heat_Life', '0013_new_preview_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='название', max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('adress', models.CharField(default='Название', max_length=300)),
                ('text', models.TextField(blank=True, verbose_name='Сообщение')),
            ],
        ),
    ]
