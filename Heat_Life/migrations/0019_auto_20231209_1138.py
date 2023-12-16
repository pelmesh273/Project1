# Generated by Django 3.2 on 2023-12-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Heat_Life', '0018_product_questions_rev'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='extra_desc',
            new_name='extra_desc_ru',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='full_desc',
            new_name='full_desc_ru',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='name_ru',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='short_desc',
            new_name='short_desc_ru',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='tech_desc',
            new_name='tech_desc_ru',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='desc',
            new_name='desc_ru',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='name',
            new_name='name_ru',
        ),
        migrations.RenameField(
            model_name='rev',
            old_name='name',
            new_name='name_ru',
        ),
        migrations.RenameField(
            model_name='rev',
            old_name='review',
            new_name='review_ru',
        ),
        migrations.RenameField(
            model_name='rev',
            old_name='title',
            new_name='title_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='language',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='language',
        ),
        migrations.RemoveField(
            model_name='rev',
            name='language',
        ),
        migrations.AddField(
            model_name='product',
            name='extra_desc_en',
            field=models.TextField(blank=True, verbose_name='Additional Information'),
        ),
        migrations.AddField(
            model_name='product',
            name='extra_desc_gr',
            field=models.TextField(blank=True, verbose_name='Επιπλέον πληροφορίες'),
        ),
        migrations.AddField(
            model_name='product',
            name='full_desc_en',
            field=models.TextField(blank=True, verbose_name='Full description'),
        ),
        migrations.AddField(
            model_name='product',
            name='full_desc_gr',
            field=models.TextField(blank=True, verbose_name='Πλήρης περιγραφή'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(default='Name', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='name_gr_gr',
            field=models.CharField(default='Ονομα', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='short_desc_en',
            field=models.TextField(blank=True, verbose_name='Short description'),
        ),
        migrations.AddField(
            model_name='product',
            name='short_desc_gr',
            field=models.TextField(blank=True, verbose_name='Σύντομη περιγραφή'),
        ),
        migrations.AddField(
            model_name='product',
            name='tech_desc_en',
            field=models.TextField(blank=True, verbose_name='Specifications'),
        ),
        migrations.AddField(
            model_name='product',
            name='tech_desc_gr',
            field=models.TextField(blank=True, verbose_name='Προδιαγραφές'),
        ),
        migrations.AddField(
            model_name='questions',
            name='desc_en',
            field=models.TextField(blank=True, verbose_name='answer'),
        ),
        migrations.AddField(
            model_name='questions',
            name='desc_gr',
            field=models.TextField(blank=True, verbose_name='απάντηση'),
        ),
        migrations.AddField(
            model_name='questions',
            name='name_en',
            field=models.CharField(default='Question', max_length=200),
        ),
        migrations.AddField(
            model_name='questions',
            name='name_gr',
            field=models.CharField(default='ερώτηση', max_length=200),
        ),
        migrations.AddField(
            model_name='rev',
            name='name_en',
            field=models.CharField(default='Name', max_length=200),
        ),
        migrations.AddField(
            model_name='rev',
            name='name_gr',
            field=models.CharField(default='Ονομα', max_length=200),
        ),
        migrations.AddField(
            model_name='rev',
            name='review_en',
            field=models.TextField(blank=True, verbose_name='Review'),
        ),
        migrations.AddField(
            model_name='rev',
            name='review_gr',
            field=models.TextField(blank=True, verbose_name='Ανασκόπηση'),
        ),
        migrations.AddField(
            model_name='rev',
            name='title_en',
            field=models.CharField(default='Title', max_length=200),
        ),
        migrations.AddField(
            model_name='rev',
            name='title_gr',
            field=models.CharField(default='Επικεφαλίδα', max_length=200),
        ),
    ]
