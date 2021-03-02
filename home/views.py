from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
#from listings.choices import price_choices, bedroom_choices, state_choices

#from listings.models import Listing
#from realtors.models import Realtor

#home page
def index(request):
    #listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    # context = {
    #     'listings': listings,
    #     'state_choices': state_choices,
    #     'bedroom_choices': bedroom_choices,
    #     'price_choices': price_choices
    # }

    return render(request, 'index.html')

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
