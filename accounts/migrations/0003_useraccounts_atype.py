# Generated by Django 3.1.7 on 2021-04-15 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profilepicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccounts',
            name='atype',
            field=models.CharField(choices=[('W', 'Worker'), ('H', 'Hirer')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
