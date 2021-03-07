from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import publishing
from django.utils import timezone

# Create your views here.
@login_required(login_url='login')
def posting(request):
    if request.method == 'POST':

        if request.POST['title'] and request.POST['type'] and request.POST['brand'] and request.POST['modelt'] and request.POST['year'] and request.POST['transmission'] and request.POST['fuel'] and request.POST['milage'] and request.FILES['icon'] and request.FILES['image'] and request.POST['price'] and request.POST['tel'] and request.POST['city']:
            publish = publishing()
            publish.title=request.POST.get('title')
            publish.type=request.POST.get('type')
            publish.brand=request.POST.get('brand')
            publish.model=request.POST.get('modelt')
            publish.year=request.POST.get('year')
            publish.fuel=request.POST.get('fuel')
            publish.milage=request.POST.get('milage')
            publish.transmission=request.POST.get('transmission')
            publish.engine=request.POST.get('engine')
            publish.icon=request.FILES.get('icon')
            publish.image=request.FILES.get('image')
            publish.description=request.POST.get('description')
            publish.condition=request.POST.get('condition')
            publish.price=request.POST.get('price')
            publish.tel=request.POST.get('tel')
            publish.city=request.POST.get('city')
            publish.address=request.POST.get('address')
            publish.pub_date=timezone.datetime.now()
            publish.owner=request.user
            publish.save()
            return redirect('/publishing/' + str(publish.id))

        else:
            return render(request,'publishing/publishing.html',{'error':'You need to fill important data'})
    else:
        return render(request,'publishing/publishing.html')

def detail(request,publish_id):
  publish = get_object_or_404(publishing, pk=publish_id)
  return render(request, 'publishing/details.html',{'publish':publish})
