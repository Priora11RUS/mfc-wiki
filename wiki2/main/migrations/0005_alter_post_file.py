# Generated by Django 4.1.2 on 2022-12-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(null=True, upload_to='file/%Y-%m-%d/', verbose_name='Прикрепить файл'),
        ),
    ]
