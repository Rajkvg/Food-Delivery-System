from django.shortcuts import render
from django.http import HttpResponse
from .models import items,customers

def index(request):
    return render(request,"food/index.html")

def order(request):
    foods = items.objects.all()
    return render(request, "food/order.html", {
        "items":foods
    })

def item(request, number):
    if request.method=='POST':
        name=request.POST["name"]
        if not name: 
            food=items.objects.get(pk=number)
            return render(request,"food/item.html",{
            "item":food,
            "number": number,
            "message": "name required."
        }) 
        email=request.POST["email"]
        if not email: 
            food=items.objects.get(pk=number)
            return render(request,"food/item.html",{
            "item":food,
            "number": number,
            "message": "email required."
        }) 
        phone=request.POST["phone"]
        if not phone: 
            food=items.objects.get(pk=number)
            return render(request,"food/item.html",{
            "item":food,
            "number": number,
            "message": "phone required."
        }) 
        address=request.POST["address"]
        if not address: 
            food=items.objects.get(pk=number)
            return render(request,"food/item.html",{
            "item":food,
            "number": number,
            "message": "address required."
        }) 
        try:
            customer=customers(name=name,email=email,phone=phone,address=address, item_id=number)
            customer.save()
            food=items.objects.get(pk=number)
            return render(request, "food/item.html", {
                "item":food,
                "number": number,
                "message": "Order Placed."
            })
        except:
            food=items.objects.get(pk=number)
            return render(request, "food/item.html", {
                "item":food,
                "number": number,
                "message": "Unable to order."
            })
    else:
        food=items.objects.get(pk=number)
        return render(request,"food/item.html",{
            "item":food,
            "number": number
        })

