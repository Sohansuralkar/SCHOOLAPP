# Generated by Django 3.1 on 2021-04-04 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_pdf_chapter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PDF',
        ),
        migrations.DeleteModel(
            name='StudyMaterial',
        ),
    ]
