# Generated by Django 4.2.3 on 2023-07-15 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_cee', '0008_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]
