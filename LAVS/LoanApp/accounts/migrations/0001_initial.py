# Generated by Django 3.0.2 on 2020-02-23 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('CIBIL_score', models.IntegerField(blank=True, null=True)),
                ('income', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_name', models.CharField(choices=[('Home Loan', 'Home Loan'), ('Car Loan', 'Car Loan'), ('Educational Loan', 'Educational Loan'), ('Personal Loan', 'Personal Loan'), ('Buisness Loan', 'Buisness Loan'), ('Gold Loan', 'Gold Loan')], max_length=200, null=True)),
                ('bank', models.CharField(blank=True, choices=[('AXIS', 'AXIS'), ('HDFC', 'HDFC'), ('ICICI', 'ICICI')], max_length=200, null=True)),
                ('Tenure', models.IntegerField(blank=True, null=True)),
                ('Processing_Fees', models.IntegerField(blank=True, null=True)),
                ('loan_amount', models.IntegerField(blank=True, null=True)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Applicant')),
            ],
        ),
    ]
