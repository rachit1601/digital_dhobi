from django.shortcuts import render, redirect
from orders.models import orders
from django.core.mail import send_mail
# Create your views here.

def order(request):
    orders_all=orders.objects.all()
    return render(request, 'orders.html', {'orders':orders_all})

def order_detail(request, order_id):
    order=orders.objects.get(id=order_id)
    return render(request, 'order_detail.html', {'order':order})

def new_order(request):
	return render(request,'form.html')

def order_submit(request):
    if request.method == 'POST':
        orders_no = orders.objects.count()
        id = orders_no + 1
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
        
        order = orders(id=id, date=date, name=name, enroll_no=enroll_no, room=room, kurta=kurta, pyjama=pyjama, shirt=shirt, tshirt=tshirt, pant=pant, lower=lower, shorts=shorts, bedsheet=bedsheet, pillowcover=pillowcover, towel=towel, dupatta=dupatta, total_clothes=total_clothes)
        order.save()
        send_mail('Your dhobi order',
        'Your order has been submitted',
                  'order@digitaldhobi.com',
                  f"{enroll_no}@bennett.edu.in",
                  fail_silently=True)
        return redirect('order_detail', order_id=order.id)

