from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from publishing.models import publishing
from django.core.paginator import Paginator

def index(request):
    publish = publishing.objects.order_by('-pub_date')

    return render(request, 'index.html',{'publish': publish })

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        #send Email
        send_mail(
           subject,#Subject
           message+ ' from '+email,#message
           email,#from
           ['denukasandeepa@gmail.com'],#to
        )

        return render(request,'contact.html',{ 'name' :  name })
    else:
        return render(request,'contact.html')

def type(request):
    type = publishing.objects.order_by('-pub_date')

    if 'sedan' in request.GET:
      sedan = request.GET['sedan']
      if sedan:
        type = type.filter(type__icontains=sedan)

    if 'suv' in request.GET:
      suv = request.GET['suv']
      if suv:
        type = type.filter(type__icontains=suv)

    if 'coupe' in request.GET:
      coupe = request.GET['coupe']
      if coupe:
        type = type.filter(type__icontains=coupe)

    if 'pickup' in request.GET:
      pickup = request.GET['pickup']
      if pickup:
        type = type.filter(type__icontains=pickup)

    if 'CUV/Crossover' in request.GET:
      Crossover = request.GET['CUV/Crossover']
      if Crossover:
        type = type.filter(type__icontains='CUV/Crossover')

    if 'Convertible' in request.GET:
      Convertible = request.GET['Convertible']
      if Convertible:
        type = type.filter(type__icontains='Convertible')

    if 'Hatchback' in request.GET:
      Hatchback = request.GET['Hatchback']
      if Hatchback:
        type = type.filter(type__icontains=Hatchback)

    if 'MPV/Minivan' in request.GET:
      MPV = request.GET['MPV/Minivan']
      if MPV:
        type = type.filter(type__icontains='MPV/Minivan')

    if 'Station Wagon' in request.GET:
      Station = request.GET['Station Wagon']
      if Station:
        type = type.filter(type__icontains='Station Wagon')

    if 'van' in request.GET:
      van = request.GET['van']
      if van:
        type = type.filter(type__icontains=van)

    if 'bus' in request.GET:
      bus = request.GET['bus']
      if bus:
        type = type.filter(type__icontains=bus)

    if 'lorry' in request.GET:
      lorry = request.GET['lorry']
      if lorry:
        type = type.filter(type__icontains=lorry)

    if 'motorbike' in request.GET:
      motorbike = request.GET['motorbike']
      if motorbike:
        type = type.filter(type__icontains=motorbike)

    if 'scooter' in request.GET:
      scooter = request.GET['scooter']
      if scooter:
        type = type.filter(type__icontains=scooter)


    if 'Three-Wheeler' in request.GET:
      Three = request.GET['Three-Wheeler']
      if Three:
        type = type.filter(type__icontains='Three-Wheeler')

    paginator = Paginator(type, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
         'count':type.count(),
         'page':paged_listings,
         'searched': request.GET
    }
    return render(request, 'publishing/search.html', context)
