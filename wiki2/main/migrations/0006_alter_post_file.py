# Generated by Django 4.1.2 on 2022-12-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='file/%Y-%m-%d/', verbose_name='Прикрепить файл'),
        ),
    ]
