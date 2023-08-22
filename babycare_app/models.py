from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Login(AbstractUser):
    user_type=models.CharField(max_length=30)
    view_password=models.CharField(max_length=30)

class Panchayat(models.Model):
    panchayat_login=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    panchayat_name=models.CharField(max_length=30)
    district=models.CharField(max_length=30)
    phone=models.CharField(max_length=30,null=True)
    email=models.EmailField(null=True)
    pin=models.CharField(max_length=30,null=True)
    wardno=models.CharField(max_length=30,null=True)
    address=models.TextField(null=True)

# class Ward(models.Model):
#     panchayat=models.ForeignKey(Panchayat,on_delete=models.CASCADE)
#     ward_name=models.CharField(max_length=30)

class Worker(models.Model):
    panchayat=models.ForeignKey(Panchayat,on_delete=models.CASCADE,null=True)
    worker_login=models.ForeignKey(Login,on_delete=models.CASCADE)
    ward=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    email=models.EmailField()
    address=models.TextField()

class Scheme(models.Model):
    scheme_name=models.CharField(max_length=30)
    scheme_desc=models.TextField()
    scheme_eligibility=models.TextField()
    scheme_procedure=models.TextField()
    published_on=models.DateField(auto_now_add=True,null=True)

class Mother(models.Model):
    mother_login=models.ForeignKey(Login,on_delete=models.CASCADE)
    worker=models.ForeignKey(Worker,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    email=models.EmailField()
    address=models.TextField()
    is_child=models.CharField(max_length=10,blank=True,null=True,default='no')
    is_pregnant=models.CharField(max_length=10,blank=True,null=True,default='no')
    pregnancy_month=models.CharField(max_length=30,blank=True)
    pregnancy_weight=models.CharField(max_length=30,blank=True,null=True)

class Child(models.Model):
    mother=models.ForeignKey(Mother,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.CharField(max_length=30)
    weight=models.CharField(max_length=30,null=True)

class Food(models.Model):
    worker=models.ForeignKey(Worker,on_delete=models.CASCADE,null=True)
    given_on=models.DateField(auto_now_add=True)
    food_list=models.CharField(max_length=30)
    unit=models.CharField(max_length=30)
    food_for=models.CharField(max_length=30,null=True)
    detail_desc=models.TextField(null=True)

class Tips(models.Model):
    worker=models.ForeignKey(Worker,on_delete=models.CASCADE)
    tip_name=models.CharField(max_length=30)
    tip_desc=models.TextField()

class Healthcentre(models.Model):
    health_login=models.ForeignKey(Login,on_delete=models.CASCADE)
    panchayat=models.ForeignKey(Panchayat,on_delete=models.CASCADE)
    health_name=models.CharField(max_length=30)
    health_address=models.TextField()
    health_phone=models.CharField(max_length=30)
    email=models.EmailField()

class Disease(models.Model):
    healthcentre=models.ForeignKey(Healthcentre,on_delete=models.CASCADE)
    disease_title=models.CharField(max_length=30)
    published_on=models.DateField(auto_now_add=True,null=True)
    disease_desc=models.TextField()
    disease_symptoms=models.TextField()
    disease_prevention=models.TextField()

class VaccinationInfo(models.Model):
    healthcentre=models.ForeignKey(Healthcentre,on_delete=models.CASCADE)
    vaccination_name=models.CharField(max_length=30)
    vaccination_desc=models.TextField()
    vaccination_age=models.CharField(max_length=30)
    disease_prevented=models.CharField(max_length=30)
    dose=models.CharField(max_length=30)
    availabecount=models.CharField(max_length=30,null=True)
    published_on=models.DateField(auto_now_add=True,null=True)
    vaccination_date=models.DateField(null=True,blank=True)
    vaccination_from=models.TimeField(null=True,blank=True)
    vaccination_to=models.TimeField(null=True,blank=True)

