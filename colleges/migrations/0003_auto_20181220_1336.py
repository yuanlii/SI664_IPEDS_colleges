# Generated by Django 2.1.4 on 2018-12-20 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0002_auto_20181215_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='graduationbyrace',
            options={'managed': False, 'ordering': ['institution_id', 'graduation_race_category_id'], 'verbose_name': 'IPEDS Institution Graduation by Race', 'verbose_name_plural': 'IPEDS Institution Graduations by Race'},
        ),
    ]