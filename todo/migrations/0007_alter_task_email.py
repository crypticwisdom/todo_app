# Generated by Django 3.2.7 on 2021-09-12 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]