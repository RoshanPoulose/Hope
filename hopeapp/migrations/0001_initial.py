# Generated by Django 5.0.1 on 2024-04-19 06:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookedTherapists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10, null=True)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hopeapp.registration')),
            ],
        ),
        migrations.CreateModel(
            name='TherapistRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('regnum', models.CharField(max_length=50, null=True)),
                ('therapy_type', models.CharField(max_length=50, null=True)),
                ('about', models.CharField(max_length=50, null=True)),
                ('hname', models.CharField(max_length=50, null=True)),
                ('fees', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('pincode', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('dateofsubmission', models.DateTimeField(auto_now_add=True, null=True)),
                ('answer', models.CharField(max_length=50, null=True)),
                ('bk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hopeapp.bookedtherapists')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hopeapp.registration')),
                ('therapy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hopeapp.therapistregistration')),
            ],
        ),
        migrations.CreateModel(
            name='PostDepressionSolutions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('solutions', models.CharField(max_length=70, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hopeapp.add_category')),
                ('therapy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hopeapp.therapistregistration')),
            ],
        ),
        migrations.AddField(
            model_name='bookedtherapists',
            name='therapy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hopeapp.therapistregistration'),
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
