# Generated by Django 5.0.3 on 2024-03-24 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_bookevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookevent',
            name='event_type',
            field=models.CharField(choices=[('checkout', 'Checkout'), ('return', 'Return'), ('reserve', 'Reserve'), ('fulfill', 'Fulfill')], max_length=20),
        ),
    ]
