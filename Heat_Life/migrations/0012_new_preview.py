# Generated by Django 3.2 on 2023-11-08 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Heat_Life', '0011_new_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='preview',
            field=models.ImageField(blank=True, upload_to='static\\media\\img'),
        ),
    ]
