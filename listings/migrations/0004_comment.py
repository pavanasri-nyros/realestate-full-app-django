# Generated by Django 3.0.3 on 2020-03-01 09:22

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20200220_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField(verbose_name='message')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('date_comment', models.DateField(default=datetime.date.today)),
                ('proid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id+', to='listings.Listing')),
            ],
        ),
    ]
