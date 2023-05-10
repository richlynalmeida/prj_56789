# Generated by Django 4.1.7 on 2023-05-03 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a_hr', '0001_initial'),
        ('z_tab_pmb_quantum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pmbl03wp',
            name='pmb_L03_wp_company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='a_hr.company', verbose_name='PMB L03 WP Company ID'),
        ),
    ]