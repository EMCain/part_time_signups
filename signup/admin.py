from django.contrib import admin

# Register your models here.

from .models import Family, Camper, AgeGroup, House, HousingRateGroup, Reservation, Rate

admin.site.register(Family)
admin.site.register(Camper)
admin.site.register(AgeGroup)
admin.site.register(House)
# admin.site.register(NightlyRate)
admin.site.register(Reservation)