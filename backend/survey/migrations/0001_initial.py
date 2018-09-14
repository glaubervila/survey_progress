# Generated by Django 2.1.1 on 2018-09-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exposure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pfw_attempt_id', models.BigIntegerField(help_text='Unique identifier for each image (1 image is composed by 62 CCDs)', verbose_name='Image Id')),
                ('nite', models.DateField(help_text='Night at which the observation was made.', verbose_name='Night')),
                ('expnum', models.BigIntegerField(help_text='Unique identifier for each image, same function as pfw_attenp_id (it also recorded in the file name)', verbose_name='Exposure')),
                ('ccdnum', models.IntegerField(help_text='CCD Number (1, 2, ..., 62)', verbose_name='CCD')),
                ('band', models.CharField(choices=[('u', 'u'), ('g', 'g'), ('r', 'r'), ('i', 'i'), ('z', 'z'), ('Y', 'Y')], help_text='Filter used to do the observation (u, g, r, i, z, Y).', max_length=1, verbose_name='Filter')),
                ('exptime', models.FloatField(help_text='Exposure time of observation.', verbose_name='Exposure time')),
                ('crossra0', models.BooleanField(default=False, verbose_name='Cross RA 0')),
                ('racmin', models.FloatField(help_text='Minimal and maximum right ascension respectively of the CCD cover.', verbose_name='racmin')),
                ('racmax', models.FloatField(help_text='Minimal and maximum right ascension respectively of the CCD cover.', verbose_name='racmax')),
                ('deccmin', models.FloatField(help_text='Minimum and maximum declination respectively of the CCD cover.', verbose_name='deccmin')),
                ('deccmax', models.FloatField(help_text='Minimum and maximum declination respectively of the CCD cover.', verbose_name='deccmax')),
                ('ra_cent', models.FloatField(help_text='Right ascension of the CCD center', verbose_name='ra_cent')),
                ('dec_cent', models.FloatField(help_text='Declination of the CCD center', verbose_name='dec_cent')),
                ('rac1', models.FloatField(help_text='CCD Corner Coordinates 1 - upper left.', verbose_name='rac1')),
                ('rac2', models.FloatField(help_text='CCD Corner Coordinates 2 - lower left.', verbose_name='rac2')),
                ('rac3', models.FloatField(help_text='CCD Corner Coordinates 3 - lower right.', verbose_name='rac3')),
                ('rac4', models.FloatField(help_text='CCD Corner Coordinates 4 - upper right).', verbose_name='rac4')),
                ('decc1', models.FloatField(help_text='CCD Corner Coordinates 1 - upper left.', verbose_name='decc1')),
                ('decc2', models.FloatField(help_text='CCD Corner Coordinates 2 - lower left.', verbose_name='decc2')),
                ('decc3', models.FloatField(help_text='CCD Corner Coordinates 3 - lower right.', verbose_name='decc3')),
                ('decc4', models.FloatField(help_text='CCD Corner Coordinates 4 - upper right).', verbose_name='decc4')),
                ('path', models.TextField(help_text='Path in the DES database where the image is stored.', verbose_name='Path')),
                ('filename', models.CharField(help_text='Name of FITS file with a CCD image.', max_length=256, verbose_name='Filename')),
                ('downloaded', models.BooleanField(default=False, help_text='flag indicating whether the image was downloaded from DES.', verbose_name='Downloaded')),
            ],
        ),
        migrations.AddIndex(
            model_name='exposure',
            index=models.Index(fields=['expnum'], name='survey_expo_expnum_560830_idx'),
        ),
        migrations.AddIndex(
            model_name='exposure',
            index=models.Index(fields=['expnum', 'ccdnum'], name='survey_expo_expnum_6342b8_idx'),
        ),
        migrations.AddIndex(
            model_name='exposure',
            index=models.Index(fields=['expnum', 'ccdnum', 'band'], name='survey_expo_expnum_35e596_idx'),
        ),
        migrations.AddIndex(
            model_name='exposure',
            index=models.Index(fields=['nite'], name='survey_expo_nite_cc544e_idx'),
        ),
        migrations.AddIndex(
            model_name='exposure',
            index=models.Index(fields=['rac1'], name='survey_expo_rac1_c5d70a_idx'),
        ),
        migrations.AddIndex(
            model_name='exposure',
            index=models.Index(fields=['rac2'], name='survey_expo_rac2_b169d3_idx'),
        ),
        migrations.AddIndex(
            model_name='exposure',
            index=models.Index(fields=['rac3'], name='survey_expo_rac3_c684e8_idx'),
        ),
        migrations.AddIndex(
            model_name='exposure',
            index=models.Index(fields=['rac4'], name='survey_expo_rac4_5cc390_idx'),
        ),
        migrations.AddIndex(
            model_name='exposure',
            index=models.Index(fields=['decc1'], name='survey_expo_decc1_17d00b_idx'),
        ),
        migrations.AddIndex(
            model_name='exposure',
            index=models.Index(fields=['decc2'], name='survey_expo_decc2_e8a7a5_idx'),
        ),
        migrations.AddIndex(
            model_name='exposure',
            index=models.Index(fields=['decc3'], name='survey_expo_decc3_405b52_idx'),
        ),
        migrations.AddIndex(
            model_name='exposure',
            index=models.Index(fields=['decc4'], name='survey_expo_decc4_3922a6_idx'),
        ),
    ]
