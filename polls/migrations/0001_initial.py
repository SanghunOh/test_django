# Generated by Django 3.2.5 on 2021-07-14 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=100)),
                ('public_date', models.DateTimeField()),
                ('votes', models.BigIntegerField()),
            ],
        ),
    ]
