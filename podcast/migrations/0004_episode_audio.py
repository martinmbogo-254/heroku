# Generated by Django 4.0.2 on 2022-02-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0003_alter_episode_options_episode_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
