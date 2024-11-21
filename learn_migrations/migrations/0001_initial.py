# Generated by Django 5.1.3 on 2024-11-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Blog Content')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('date_published', models.DateField(verbose_name='Publication Date')),
            ],
        ),
    ]