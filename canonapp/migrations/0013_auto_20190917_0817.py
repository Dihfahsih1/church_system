# Generated by Django 2.1.7 on 2019-09-17 05:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('canonapp', '0012_auto_20190330_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 5, 17, 18, 621809, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='driver_checklist',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 5, 17, 18, 623741, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='driver_payment_report',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 5, 17, 18, 622718, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='driver_payment_reports_archive',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 5, 17, 18, 623741, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='driverpayment',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 5, 17, 18, 621809, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='driverpayments_archive',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 5, 17, 18, 622718, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expensesreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 5, 17, 18, 625800, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='salary',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 5, 17, 18, 624713, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='salaryreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 5, 17, 18, 625800, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spend',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 5, 17, 18, 624713, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sundry',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 5, 17, 18, 624713, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sundryreportarchive',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 5, 17, 18, 625800, tzinfo=utc)),
        ),
    ]
