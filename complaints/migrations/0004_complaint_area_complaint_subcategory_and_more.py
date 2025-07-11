# Generated by Django 5.2.1 on 2025-05-21 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0003_alter_complaint_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='area',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='subcategory',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='category',
            field=models.CharField(choices=[('WATER', 'Water'), ('Hostel', 'Hostel'), ('Elctricity', 'Electricity'), ('Other', 'Other')], default='Other', max_length=50),
        ),
    ]
