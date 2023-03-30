# Generated by Django 4.1.7 on 2023-03-30 02:48

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.TimeField()),
                ('apellido', models.TimeField()),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('password', models.TextField()),
                ('tipousuario', models.CharField(choices=[('ADMIN', 'ADMIN'), ('CLIENTE', 'CLIENTE')], db_column='tipo_usuario', max_length=100)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'usuario',
            },
            managers=[
                ('objectes', django.db.models.manager.Manager()),
            ],
        ),
    ]
