# Generated by Django 3.2.15 on 2022-08-10 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=250)),
                ('member_img', models.ImageField(upload_to='pics')),
                ('member_desc', models.TextField()),
            ],
        ),
    ]
