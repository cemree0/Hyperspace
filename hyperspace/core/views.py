from django.shortcuts import render
from services.models import Service

def index(request):

   static_content = """
   <div class="inner">
    <h1>Hyperspace</h1>
    <p>Just another fine responsive site template designed by <a href="http://html5up.net">HTML5 UP</a><br />
    and released for free under the <a href="http://html5up.net/license">Creative Commons</a>.</p>
    <ul class="actions">
        <li><a href="#one" class="button scrolly">Learn more</a></li>
    </ul>
    </div>
   """
 
   featured_services = Service.objects.filter(is_featured= True)

   context = {                            
     'static_content': static_content, 
     'featured_services' : featured_services
   }
   #context burada python sozlugudur yani {} ile acılır içinde key ve value girilir mesela  'ad' : 'cemre' sonra bu HTML de <p>Merhaba {{ ad }}</p> olarak cagirilir ve cemre yazılır .
#HTML şablonuna hangi verilerin gönderileceğini söyleyen sözlük  bu arada ismi context olmak zorunda degil ama sozluk haline getirilmelidir renderde işe yaraması için.

   return render(request, 'core/index.html', context)
# render içindeki3. sey sozluk olmalı 
# neden diretk 3.yere static_content yazmamaızın sebebi o bir sozluk degil bir string yani mesel abir key ve value yokyukarıda gosterdigim gibi.
# yani  string olan static_content i sozlugun degeri(value) olarak degiştiriyoz. yani dolaylı yoldan context uzerinde sablona geciyor.