# Generated by Django 3.0.3 on 2020-02-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20200216_0611'),
    ]

    operations = [
        migrations.CreateModel(
            name='todosfalse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
