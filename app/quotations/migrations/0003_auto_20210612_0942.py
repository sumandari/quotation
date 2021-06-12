# Generated by Django 3.2.4 on 2021-06-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0002_create_agent_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='cov_others',
            field=models.DecimalField(decimal_places=2, help_text='Flood, Windstorm, Landslide or Subsidence coverage.', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='cov_passanger_liability',
            field=models.DecimalField(decimal_places=2, help_text='Passanger Liability coverage.', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='cov_windscreen',
            field=models.DecimalField(decimal_places=2, help_text='Windscreen coverage.', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='email',
            field=models.EmailField(help_text="Customer's email.", max_length=254),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='vehicle_number',
            field=models.CharField(help_text='Vehicle No.', max_length=20),
        ),
    ]