# Generated by Django 3.2.7 on 2021-09-12 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_alter_task_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
