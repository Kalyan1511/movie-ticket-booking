from django.shortcuts import render, redirect, get_object_or_404
from .models import Slot, Booking

def home(request):
    from .models import Slot

def home(request):
    if Slot.objects.count() == 0:
        times = [
            "9:00 AM", "10:00 AM", "11:00 AM",
            "12:00 PM", "1:00 PM", "2:00 PM"
        ]
        for t in times:
            Slot.objects.create(time=t)

    slots = Slot.objects.all()
    bookings = Booking.objects.all()
    booked_slots = [b.slot.id for b in bookings]

    return render(request, 'home.html', {
        'slots': slots,
        'booked_slots': booked_slots
    })

def book_slot(request, id):
    slot = get_object_or_404(Slot, id=id)

    if Booking.objects.filter(slot=slot).exists():
        return redirect('home')  # prevent double booking

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name and email:
            Booking.objects.create(slot=slot, name=name, email=email)

    return redirect('home')


def booked_slots(request):
    bookings = Booking.objects.all()
    return render(request, 'booked.html', {'bookings': bookings})

def unbook_slot(request, id):
    booking = Booking.objects.filter(slot_id=id).first()
    
    if booking:
        booking.delete()
    
    return redirect('home')