# Generated by Django 4.1.6 on 2023-02-15 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kevinPhone', '0003_contact_contact_pass1_contact_contact_pass2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_pass1',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_pass2',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
