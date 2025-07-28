from django.db import models
from django.utils.text import slugify
#BU MODELS KLASİK SQL YONTEMLERİYLE DEGİLDE PYTHON CLASSINDA FAYDALANILDI BUNA DA PYTHON JARGONUNDA MODEL DENİLİR Yani model dosyasında faydanıldı.
# Create your models here.
#Service adlı yeni bir sınıf (class) oluşturuyorum, bu sınıf, models.Model adlı başka bir sınıftan miras alıyor (kalıtım).
#Parantez içine aldığın kısım (örneğin models.Model) senin sınıfının dayandığı temel yapıdır.
class Service(models.Model):  # models.Model demek → "models modülünün içindeki Model sınıfı" demektir.
    title = models.CharField(max_length=100)
    desciption =models.TextField()
    icon_class = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank =True )


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Service, self).save(*args, **kwargs)

    class Meta:
        ordering =['title']
        verbose_name ='Service'
        verbose_name_plural ='Services'


#Slug = başlığın URL’ye uygun, sadeleştirilmiş şekli. (Boşluk → -, büyük harf → küçük harf, özel karakterler atılır)
#slugify, bir metni slug hâline çeviren bir Python fonksiyonudur.
#slugify("Yapay Zeka") → "yapay-zeka"
