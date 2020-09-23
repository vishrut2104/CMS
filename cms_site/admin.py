from django.contrib import admin
from cms_site.models import Film
from cms_site.models import Customer
from cms_site.models import Room
from cms_site.models import Screening
from cms_site.models import Seat
from cms_site.models import Booking
from cms_site.models import Reserved_seat

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'length_min')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_seats')

class ScreeningAdmin(admin.ModelAdmin):
    list_display = ('film', 'room', 'start_time')

class SeatAdmin(admin.ModelAdmin):
    list_display = ('row_id', 'seat_number', 'room')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('screening', 'customers')

class Reserved_seatAdmin(admin.ModelAdmin):
    list_display = ('booking', 'seat')

admin.site.register(Film,FilmAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Screening,ScreeningAdmin)
admin.site.register(Seat,SeatAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Reserved_seat,Reserved_seatAdmin)

# Register your models here.
