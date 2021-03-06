# Generated by Django 3.0.3 on 2020-07-21 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
