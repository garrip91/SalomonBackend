# Generated by Django 3.2.5 on 2021-07-12 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [

        migrations.AddField(
            model_name='good',
            name='ability_to_twist',
            field=models.BooleanField(default=False, verbose_name='Возможность скрутить'),
        ),
        migrations.AddField(
            model_name='good',
            name='height',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='good',
            name='hypoallergenic',
            field=models.BooleanField(default=False, verbose_name='Гипоаллергенный'),
        ),
        migrations.AddField(
            model_name='good',
            name='mattress_type',
            field=models.CharField(blank=True, max_length=50, verbose_name='Тип матраса'),
        ),
        migrations.AddField(
            model_name='good',
            name='maximum_load_on_one_berth',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Макс. нагрузка на одно спальное место'),
        ),
        migrations.AddField(
            model_name='goods_cart',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='order',
            name='telephone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='slides',
            name='url',
            field=models.URLField(default=''),
        ),
    ]
