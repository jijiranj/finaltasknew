

# Create your models here.

from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


class District(models.Model):
    dist = models.CharField(max_length=250)
    deta = models.TextField()

    def __str__(self):
        return self.dist


class SubBranches(models.Model):
    dist= models.ForeignKey(District,on_delete=models.CASCADE)
    sub=models.CharField(max_length=250)

    def __str__(self):
        return self.sub

class contactdetails(models.Model):
    nam = models.CharField(max_length=100)
    dist = models.ForeignKey(District,on_delete=models.CASCADE)
    branches = models.CharField(max_length=250)
    def __str__(self):
        return self.nam







# class employee(models.Model):
#     name = models.CharField(max_length=100)
#     dob = models.DateField()
#     age = models.IntegerField()
#     GENDER_CHOICES = (
#                  ("male", "Male"),
#                ("female", "Female"),
#             ("Transgender", "Transgender")
#              )
#     gender = models.CharField(choices=GENDER_CHOICES,max_length=13)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     address = models.CharField(max_length=1024)
#     email = models.EmailField(blank=True, null=True)
#     password = models.CharField(max_length=13)
#     district = models.ForeignKey(Branches, on_delete=models.CASCADE)
#     branches = models.CharField(max_length=250)
# class UserDetails(models.Model):
#     name = models.CharField(max_length=100)
#     dob = models.DateField()
#     age = models.IntegerField()
#     GENDER_CHOICES = (
#         ("male", "Male"),
#         ("female", "Female"),
#         ("Transgender", "Transgender")
#     )
#     gender = models.CharField(choices=GENDER_CHOICES)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)
#     password = models.CharField()
#     address = models.CharField(max_length=1024)
#     district = models.ForeignKey(Branches, on_delete=models.CASCADE)
#     branches = models.ForeignKey(subbranches, on_delete=models.CASCADE)
#     ACCOUNT_CHOICES = (
#         ("savings", "Savings"),
#         ("current", "Current")
#     )
#     account_type = models.CharField(choices=ACCOUNT_CHOICES)
#     M_CHOICES = (
#         ("Debit Card"),
#         ("Credit Card"),
#         ("Cheque Book")
#     )
#     materials_required = models.CharField(choices=M_CHOICES)
#
#
#     def __str__(self):
#         return self.name




