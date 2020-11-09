# Generated by Django 2.2.11 on 2020-11-09 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achivement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achivement_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingCertificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upcoming_certificate_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('collaboration_ready', models.BooleanField(default=True)),
                ('school_name', models.CharField(max_length=250)),
                ('activity_id', models.IntegerField(blank=True, null=True)),
                ('mentor_id', models.IntegerField(blank=True, null=True)),
                ('no_of_classes', models.IntegerField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=250, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=250, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('achivements', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='achivement', to='user_api.Achivement')),
                ('badges', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='badge', to='user_api.Badge')),
                ('certificates', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='user_api.Certificate')),
                ('upcoming_certificates', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upcoming_certificate', to='user_api.UpcomingCertificate')),
            ],
        ),
    ]