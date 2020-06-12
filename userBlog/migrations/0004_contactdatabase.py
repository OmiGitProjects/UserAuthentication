# Generated by Django 3.0.6 on 2020-06-12 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userBlog', '0003_auto_20200612_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=5000)),
            ],
        ),
    ]
