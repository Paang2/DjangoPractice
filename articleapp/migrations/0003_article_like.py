# Generated by Django 3.2.9 on 2021-11-26 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0002_article_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]