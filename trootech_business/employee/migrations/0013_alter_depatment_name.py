# Generated by Django 4.1.6 on 2023-02-22 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0012_alter_depatment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depatment',
            name='name',
            field=models.CharField(choices=[('DEVLOPER', 'Developer'), ('CTO', 'CTO'), ('HR', 'HR'), ('ADMIN', 'Admin')], default='HR', max_length=20),
        ),
    ]