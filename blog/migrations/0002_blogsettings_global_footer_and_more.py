# Generated by Django 4.1.7 on 2023-03-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogsettings',
            name='global_footer',
            field=models.TextField(blank=True, default='', null=True, verbose_name='公共尾部'),
        ),
        migrations.AddField(
            model_name='blogsettings',
            name='global_header',
            field=models.TextField(blank=True, default='', null=True, verbose_name='公共头部'),
        ),
    ]
