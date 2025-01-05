from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

class House(models.Model):
    owner_id = models.IntegerField(null=True)  # 可以为空
    house_number = models.CharField(max_length=20)
    area = models.FloatField()
    location = models.CharField(max_length=100)
    layout = models.CharField(max_length=50)
    monthly_rent = models.FloatField()
    status = models.CharField(max_length=20)
    available_from = models.DateField(null=True)
    lease_terms = models.CharField(max_length=255)

class Tenant(models.Model):
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=100, null=True)
    full_name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=30, null=True)

class LeaseRecord(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.FloatField()
    payment_status = models.CharField(max_length=50)
