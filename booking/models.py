from django.db import models

class Slot(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.date} - {self.time}"


class Booking(models.Model):
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.slot.time} - {self.name}"