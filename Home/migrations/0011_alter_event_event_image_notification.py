# Generated by Django 5.1.4 on 2024-12-12 08:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_alter_profile_profile_pic'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, default='events/Rectangle 2.png', null=True, upload_to='events/'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
