# Generated by Django 2.2.9 on 2020-01-21 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Enter your Facebook URL')),
                ('twitter', models.URLField(blank=True, help_text='Enter your Twitter URL')),
                ('youtube', models.URLField(blank=True, help_text='Enter your YouTube URL')),
                ('instagram', models.URLField(blank=True, help_text='Enter your Instagram URL')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
