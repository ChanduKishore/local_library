# Generated by Django 3.2.6 on 2021-08-13 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'permissions': (('can_mark_returned', 'set book as returned'),)},
        ),
    ]
