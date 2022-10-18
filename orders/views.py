from django.shortcuts import render, redirect
from orders.models import Order

# Create your views here.

def order(request):
    orders=Order.objects.all()
    return render(request, 'order.html', {'orders':orders})

def order_detail(request, order_id):
    order=Order.objects.get(id=order_id)
    return render(request, 'order_detail.html', {'order':order})

def new_order(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        date = request.POST.get('date')
        name = request.POST.get('name')
        enroll_no = request.POST.get('enroll_no')
        room = request.POST.get('room')
        kurta = request.POST.get('kurta')
        pyjama = request.POST.get('pyjama')
        shirt = request.POST.get('shirt')
        tshirt = request.POST.get('tshirt')
        pant = request.POST.get('pant')
        lower = request.POST.get('lower')
        shorts = request.POST.get('shorts')
        bedsheet = request.POST.get('bedsheet')
        pillowcover = request.POST.get('pillowcover')
        towel = request.POST.get('towel')
        dupatta = request.POST.get('dupatta')
        total_clothes = request.POST.get('total_clothes')
        
        order = Order(id=id, date=date, name=name, enroll_no=enroll_no, room=room, kurta=kurta, pyjama=pyjama, shirt=shirt, tshirt=tshirt, pant=pant, lower=lower, shorts=shorts, bedsheet=bedsheet, pillowcover=pillowcover, towel=towel, dupatta=dupatta, total_clothes=total_clothes)
        order.save()
        return redirect('order_overview')

