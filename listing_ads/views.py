from django.shortcuts import render
from django.http import HttpResponse


#listings
def main(request):
  return render(request, 'listings/listings.html')

#like button
def like(request):
    return render(request, 'listings.html')
#single listing view
def listing(request):
  return render(request, 'listings/adverticement.html')

#search bar
def search(request):



  return render(request, 'listings/search.html')
