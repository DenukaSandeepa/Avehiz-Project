from django.shortcuts import render, redirect
from django.http import HttpResponse

#listings
def listings(request):
  return render(request, 'listings/listings.html')

#like button
def like(request):
    return render(request, 'listings.html')
