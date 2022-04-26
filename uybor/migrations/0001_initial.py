# Generated by Django 4.0.3 on 2022-04-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uylar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('viloyat', models.CharField(choices=[('7', 'Samarqand'), ('11', 'Navoiy'), ('5', 'Namangan'), ('4', 'Andijon'), ('12', "Qoraqalpog'iston"), ('9', 'Qashqadaryo'), ('1', 'Toshkent Shahar'), ('10', 'Surxandaryo'), ('8', 'Xorazm'), ('3', "Farg'ona"), ('2', 'Toshkent Viloyat'), ('6', 'Buxoro')], default=1, max_length=100, verbose_name='Viloyat')),
                ('tuman', models.CharField(max_length=250, verbose_name='Tuman')),
                ('orentir', models.CharField(max_length=250, verbose_name='Orentir')),
                ('qurilish_yili', models.IntegerField(verbose_name='Qurilgan Yili')),
                ('uy_turi', models.CharField(choices=[('1', 'Ijara'), ('2', 'Sotuv')], default=1, max_length=100, verbose_name='Tanlang')),
                ('xonalar_soni', models.CharField(choices=[('5', '5'), ('2', '2'), ('3', '3'), ('1', '1'), ('4', '4'), ('6', '6')], default=2, max_length=1, verbose_name='Xonalar Soni')),
                ('jami_qavat', models.IntegerField(verbose_name='Jami Qavat')),
                ('qavat', models.IntegerField(verbose_name='Qavat')),
                ('bino_asosi', models.CharField(choices=[('2', 'Panel'), ('1', "G'ishtli")], default=1, max_length=100, verbose_name='Bino Asosi')),
                ('narxi', models.FloatField(verbose_name='Narxi')),
                ('Aftoturargox', models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=1, max_length=100, verbose_name='Aftoturargox')),
                ('lift', models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=2, max_length=100, verbose_name='Lift')),
                ('qoriqlash', models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=2, max_length=100, verbose_name="Qo'riqlash")),
                ('video_kuzatuv', models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=1, max_length=100, verbose_name='Video Kuzatuv')),
                ('kanalizatsiya', models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=1, max_length=100, verbose_name='Kanalizatsiya')),
                ('bolalar_maydonchasi', models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=1, max_length=100, verbose_name='Bolalar Maydonchasi')),
                ('internet', models.CharField(choices=[('2', "Yo'q"), ('1', 'Bor')], default=1, max_length=5, verbose_name='Internet')),
                ('qoshimcha_izoh', models.TextField(verbose_name='Izoh')),
                ('rasm', models.ImageField(upload_to='images/', verbose_name='Uy Rasmi')),
                ('uy_egasi', models.CharField(max_length=50, verbose_name='Uy Egasi')),
                ('telefon_raqami', models.CharField(max_length=14, verbose_name="Bog'lanish")),
            ],
        ),
    ]