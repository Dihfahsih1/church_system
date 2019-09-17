# Generated by Django 2.1.7 on 2019-03-02 11:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('canonapp', '0003_auto_20190301_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 2, 11, 51, 3, 445095, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_monthly_payment',
            field=models.FloatField(default=1104000.0),
        ),
        migrations.AlterField(
            model_name='driver_payment_report',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 2, 11, 51, 3, 446045, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='driver_payment_reports_archive',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 2, 11, 51, 3, 446934, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='driverpayment',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 2, 11, 51, 3, 445595, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='driverpayments_archive',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 2, 11, 51, 3, 446435, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='salary',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 2, 11, 51, 3, 447922, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spend',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 2, 11, 51, 3, 448818, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sundry',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 3, 2, 11, 51, 3, 448413, tzinfo=utc)),
        ),
    ]