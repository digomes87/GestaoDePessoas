# Generated by Django 2.1.5 on 2020-06-04 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_auto_20200604_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionarios',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa'),
        ),
    ]
