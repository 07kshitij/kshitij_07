# Generated by Django 2.0.9 on 2019-01-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='down',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='up',
            field=models.IntegerField(default=0),
        ),
    ]