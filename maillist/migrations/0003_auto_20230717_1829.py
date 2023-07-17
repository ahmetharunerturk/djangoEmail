# Generated by Django 3.2.5 on 2023-07-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maillist', '0002_emaillist_delete_maillistesi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emaillist',
            name='subscribers',
        ),
        migrations.AddField(
            model_name='emaillist',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
