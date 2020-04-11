# Generated by Django 3.0.4 on 2020-03-26 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=15)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=15)),
                ('state_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CarOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dateOfBirth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_the_beginning', models.DateField()),
                ('date_of_expiration', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.CarOwner')),
                ('state_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Car')),
            ],
        ),
        migrations.CreateModel(
            name='DriverDocument',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_issue', models.DateField()),
                ('type', models.CharField(choices=[('A', 'Motorcycle'), ('A1', 'Light motorcycle'), ('B', 'Light car, small truck'), ('BE', 'Car with trailer'), ('B1', 'Tricycle'), ('C', 'Truck'), ('CE', 'Truck with trailer'), ('C1', 'Medium truck'), ('C1E', 'Medium truck with trailer'), ('D', 'Bus'), ('DE', 'Bus with truck'), ('D1', 'Small bus'), ('D1E', 'Small bus with truck'), ('M', 'Moped'), ('Tm', 'Tram'), ('Tb', 'Trolleybus')], max_length=3)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.CarOwner')),
            ],
        ),
    ]