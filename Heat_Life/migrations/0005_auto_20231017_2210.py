# Generated by Django 3.2 on 2023-10-17 15:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Heat_Life', '0004_category_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='news_block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Название', max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='static\\media\\img')),
                ('full_desc', models.TextField(blank=True, verbose_name='Текст блока')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='my_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='news',
            name='news_block',
            field=models.ManyToManyField(blank=True, null=True, related_name='news', to='Heat_Life.news_block'),
        ),
    ]
