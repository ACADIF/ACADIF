# Generated by Django 4.1 on 2022-09-23 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('aluno', '0003_alter_aluno_rg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais_aluno',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='pai de aluno +', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('endereco', models.CharField(max_length=120)),
                ('born', models.DateField()),
                ('cpf', models.IntegerField()),
                ('telefone', models.CharField(max_length=15)),
                ('rg', models.CharField(max_length=9)),
                ('filho', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='filho', to='aluno.aluno')),
            ],
        ),
    ]
