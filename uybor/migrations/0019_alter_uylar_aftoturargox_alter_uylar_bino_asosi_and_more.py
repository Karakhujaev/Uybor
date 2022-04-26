# Generated by Django 4.0.3 on 2022-04-26 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uybor', '0018_alter_uylar_aftoturargox_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uylar',
            name='Aftoturargox',
            field=models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=1, max_length=100, verbose_name='Aftoturargox'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='bino_asosi',
            field=models.CharField(choices=[('2', 'Panel'), ('1', "G'ishtli")], default=1, max_length=100, verbose_name='Bino Asosi'),
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
            field=models.CharField(choices=[('1', 'Ijara'), ('2', 'Sotuv')], default=1, max_length=100, verbose_name='Tanlang'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='video_kuzatuv',
            field=models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=1, max_length=100, verbose_name='Video Kuzatuv'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='viloyat',
            field=models.CharField(choices=[('5', 'Namangan'), ('10', 'Surxandaryo'), ('3', "Farg'ona"), ('12', "Qoraqalpog'iston"), ('7', 'Samarqand'), ('11', 'Navoiy'), ('2', 'Toshkent Viloyat'), ('8', 'Xorazm'), ('1', 'Toshkent Shahar'), ('4', 'Andijon'), ('9', 'Qashqadaryo'), ('6', 'Buxoro')], default=1, max_length=100, verbose_name='Viloyat'),
        ),
        migrations.AlterField(
            model_name='uylar',
            name='xonalar_soni',
            field=models.CharField(choices=[('2', '2'), ('1', '1'), ('6', '6'), ('4', '4'), ('3', '3'), ('5', '5')], default=2, max_length=1, verbose_name='Xonalar Soni'),
        ),
    ]
