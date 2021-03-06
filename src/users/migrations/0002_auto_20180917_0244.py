# Generated by Django 2.1.1 on 2018-09-17 02:44

from django.db import migrations, models
import users.validations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='CPF',
            field=models.CharField(max_length=13, unique=True, validators=[users.validations.validate_cpf, users.validations.validate_cpf_length]),
        ),
        migrations.AlterField(
            model_name='user',
            name='RG',
            field=models.CharField(max_length=11, unique=True, validators=[users.validations.validate_rg_length]),
        ),
    ]
