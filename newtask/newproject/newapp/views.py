from django.shortcuts import render
from .models import place
from .models import details


# Create your views here.
def newweb(request):
    obj = place.objects.all()
    new = details.objects.all()
    return render(request, "index.html", {'result': obj, 'result2': new})
