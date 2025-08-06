from django.shortcuts import render 
from . models import Service
# Create your views here.

def service_list(request):
    services = Service.objects.all()
    #Service.objects → “Service tablosuyla çalışmak istiyorum” demek.
    #Parantezler (()) burada önemli çünkü:
    #Parantez çağırma anlamına gelir.
    #all sadece bir fonksiyonun adı,
    #all() ise “bu fonksiyonu çalıştır” demektir.


    return render(request, 'services/service_list.html',{'services':services})