# Generated by Django 4.1 on 2022-09-27 02:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('media_page', '0002_alter_photo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('video', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('upload_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
