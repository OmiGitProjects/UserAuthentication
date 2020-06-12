# Generated by Django 3.0.6 on 2020-06-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBlogsDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(max_length=105)),
                ('blogContent', models.TextField(max_length=5000)),
                ('images', models.ImageField(upload_to='blogImages/')),
                ('slug', models.CharField(max_length=105)),
                ('blogTimeStamp', models.DateField()),
            ],
        ),
    ]
