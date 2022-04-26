# Generated by Django 4.0.3 on 2022-04-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uybor', '0016_alter_uylar_viloyat_alter_uylar_xonalar_soni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uylar',
            name='Aftoturargox',
            field=models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=1, max_length=100, verbose_name='Aftoturargox'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='bolalar_maydonchasi',
            field=models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=1, max_length=100, verbose_name='Bolalar Maydonchasi'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='internet',
            field=models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=1, max_length=5, verbose_name='Internet'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='kanalizatsiya',
            field=models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=1, max_length=100, verbose_name='Kanalizatsiya'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='lift',
            field=models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=2, max_length=100, verbose_name='Lift'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='qoriqlash',
            field=models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=2, max_length=100, verbose_name="Qo'riqlash"),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='uy_turi',
            field=models.CharField(choices=[('2', 'Sotuv'), ('1', 'Ijara')], default=1, max_length=100, verbose_name='Tanlang'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='video_kuzatuv',
            field=models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=1, max_length=100, verbose_name='Video Kuzatuv'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='viloyat',
            field=models.CharField(choices=[('2', 'Toshkent Viloyat'), ('9', 'Qashqadaryo'), ('10', 'Surxandaryo'), ('8', 'Xorazm'), ('1', 'Toshkent Shahar'), ('4', 'Andijon'), ('12', "Qoraqalpog'iston"), ('11', 'Navoiy'), ('6', 'Buxoro'), ('3', "Farg'ona"), ('5', 'Namangan'), ('7', 'Samarqand')], default=1, max_length=100, verbose_name='Viloyat'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='xonalar_soni',
            field=models.CharField(choices=[('4', '4'), ('5', '5'), ('6', '6'), ('3', '3'), ('1', '1'), ('2', '2')], default=2, max_length=1, verbose_name='Xonalar Soni'),
        ),
    ]