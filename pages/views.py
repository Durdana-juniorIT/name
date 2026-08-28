from django.shortcuts import render, HttpResponse


def index(request):
   flag = 20
   products = [
      {'title': 'apple', 'price': 200},
      {'title': 'banana', 'price': 150},
      {'title': 'orange', 'price': 100},
   ]
   data = {
       'flag': flag,
       'products': products,
    }
   return render(request,  'index.html', context=data) 


def about(request):
    return render(request,  'about.html', context={}) 


def contact(request):
    return render(request,  'contact.html', context={})