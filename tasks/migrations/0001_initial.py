# Generated by Django 3.1.4 on 2021-03-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'To do'), (1, 'In progress'), (2, 'Done')])),
            ],
        ),
    ]