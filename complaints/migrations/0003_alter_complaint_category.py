# Generated by Django 5.2.1 on 2025-05-21 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0002_complaint_category_complaint_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='category',
            field=models.CharField(choices=[('WATER', 'Water'), ('Hostel', 'Hostel'), ('Elctricity', 'Elctricity'), ('Other', 'Other')], default='Other', max_length=50),
        ),
    ]
