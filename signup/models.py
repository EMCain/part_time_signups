from django.db import models
from django.contrib.auth.models import User

from djorm_pgarray.fields import DateArrayField

from datetime import date

# the person who signs up
class Family(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    user = models.ForeignKey(User)

    def __str__(self):
        return "Family of " + self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return "Family of " + self.first_name + ' ' + self.last_name


# listing of age groups
class AgeGroup(models.Model):
    name = models.CharField(max_length=25)
    program_fee = models.DecimalField(decimal_places=2, max_digits=6) # one time fee for the entire week

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# the person who is attending camp
class Camper(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age_group = models.ForeignKey(AgeGroup, default=1)

    def __str__(self):
        return "Camper " + self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return "Camper " + self.first_name + ' ' + self.last_name


# this is kind of silly but I can't find a better way to do many-to-many between houses and rates
class HousingRateGroup(models.Model):

    def __str__(self):
        return "rate group " +  self.id

    def __unicode__(self):
        return "rate group " + self.id

class House(models.Model):
    name = models.CharField(max_length=25)
    hr_group = models.ForeignKey(HousingRateGroup, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

#
# # each of these is a rate listing
# # if someone wants to do this as something more complex than $x/ night, they can write the formula.
# # until then: it's UCC weekly rate/5.
# class NightlyRate(models.Model):
#     house = models.ForeignKey(House)
#     age_group = models.ForeignKey(AgeGroup)
#     base_rate = models.DecimalField(decimal_places=2, max_digits=6, default=0) # base cost
#     nightly_rate = models.DecimalField(decimal_places=2, max_digits=6, default=0) # cost per night
#     is_single = models.BooleanField(default=False) # i.e. has this person reserved a room entirely for themselves
#
#     def __str__(self):
#         return "$" + str(self.nightly_rate) + " per night for " + str(self.age_group) + " in " + str(self.house) + " -- single: " + str(self.is_single)
#
#     def __unicode__(self):
#         return "$" + unicode(self.nightly_rate) + " per night for " + self.age_group + " in " + self.house + " -- single: " + unicode(self.is_single)

class Reservation(models.Model):
    camper = models.ForeignKey(Camper)
    year = models.IntegerField(null=True)
    dates = DateArrayField()
    last_modified = models.DateTimeField()

    def __str__(self):
        return 'Reservation: ' + str(self.camper) + " " + str(self.year)

    def __unicode__(self):
        return 'Reservation: ' + unicode(self.camper) + " " + unicode(self.year)


class Rate(models.Model):
    hr_group = models.ForeignKey(HousingRateGroup, null=True)
    age_group = models.ForeignKey(AgeGroup)
    is_camp_rate = models.BooleanField(default=True) # True = Seabeck rate, False = UCC rate
    year = models.IntegerField(max_length=4, default=0)

    rate_1 = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    rate_2 = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    rate_3 = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    rate_4 = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    rate_5 = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    rate_6 = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    rate_7 = models.DecimalField(decimal_places=2, max_digits=6, default=0)




