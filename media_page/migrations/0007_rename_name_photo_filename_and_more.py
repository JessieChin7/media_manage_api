# Generated by Django 4.1 on 2022-09-28 01:54

from django.db import migrations, models
import media_page.fields


class Migration(migrations.Migration):

    dependencies = [
        ('media_page', '0006_alter_video_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='name',
            new_name='filename',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='upload_date',
            new_name='upload_timestamp',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='name',
            new_name='filename',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='upload_date',
            new_name='upload_timestamp',
        ),
        migrations.AddField(
            model_name='photo',
            name='type',
            field=models.CharField(default='image', max_length=500),
        ),
        migrations.AddField(
            model_name='photo',
            name='uid',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='type',
            field=models.CharField(default='video', max_length=500),
        ),
        migrations.AddField(
            model_name='video',
            name='uid',
            field=models.CharField(blank=True, default='uid', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=media_page.fields.RestrictedFileField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=media_page.fields.RestrictedFileField(blank=True, null=True, upload_to='video/'),
        ),
    ]
