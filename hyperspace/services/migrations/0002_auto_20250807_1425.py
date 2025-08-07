from django.db import migrations

class Migration(migrations.Migration):

    # Bu migration'ın hangi migration dosyasına bağlı olduğunu belirtiyoruz.
    dependencies = [
        ('services', '0001_initial'),  # İlk migration dosyanızın adı (tablo oluşturma)
    ]

    operations = [
        # Burada, Service modelindeki 'desciption' alanının ismini 'description' olarak değiştiriyoruz.
        # Bu işlem veritabanındaki sütun adını günceller, veriler kaybolmaz.
        migrations.RenameField(
            model_name='service',        # Model adı
            old_name='desciption',       # Eski (yanlış yazılmış) alan adı
            new_name='description',      # Yeni (doğru) alan adı
        ),
    ]


# Veritabanındaki 'desciption' sütununu doğru olan 'description' olarak yeniden adlandırıyoruz.

