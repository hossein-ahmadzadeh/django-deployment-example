# Generated by Django 4.1.7 on 2023-04-20 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portofilo_site',
            new_name='portfolio_site',
        ),
    ]
