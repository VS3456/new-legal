# Generated by Django 3.1.6 on 2021-06-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210626_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contact',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='pic',
            field=models.ImageField(default='client.png', null=True, upload_to='users/client'),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='city',
            field=models.CharField(default='', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='contact',
            field=models.CharField(default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='experience',
            field=models.FloatField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='lawyertype',
            field=models.CharField(default='', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='pic',
            field=models.ImageField(default='lawyer.png', null=True, upload_to='users/laywers'),
        ),
    ]