<<<<<<< HEAD
# Generated by Django 4.1.7 on 2023-02-21 11:25
=======
# Generated by Django 4.1.7 on 2023-02-21 11:19
>>>>>>> main

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
        ),
    ]
