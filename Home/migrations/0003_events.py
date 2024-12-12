# Generated by Django 5.1.4 on 2024-12-06 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_usercredentials_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=150)),
                ('event_start', models.DateTimeField()),
                ('event_end', models.DateTimeField()),
                ('event_location', models.CharField(max_length=150)),
                ('event_description', models.TextField()),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('event_capacity', models.IntegerField()),
                ('event_image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('public_or_private', models.BooleanField()),
            ],
        ),
    ]
