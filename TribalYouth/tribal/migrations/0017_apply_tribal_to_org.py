# Generated by Django 2.2.6 on 2020-01-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribal', '0016_auto_20200118_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply_tribal_to_org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tribalemail', models.CharField(default='', max_length=80)),
                ('orgemail', models.CharField(default='', max_length=80)),
                ('application', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]
