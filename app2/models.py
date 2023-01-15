from django.db import models

class survey(models.Model):
    Name=models.CharField(max_length=250)
    Phonenumber=models.BigIntegerField()
    age=models.IntegerField()
    occupation=models.CharField(max_length=250)
    gender=models.CharField(max_length=250)
    medium=models.CharField(max_length=250)
    problem=models.CharField(max_length=250)
    easy=models.CharField(max_length=250)
    price=models.CharField(max_length=250)
    comparison=models.CharField(max_length=250)
class surveyB(models.Model):
    Name=models.CharField(max_length=250)
    Have_smartphone=models.CharField(max_length=250)
    which_phone=models.CharField(max_length=250)
    factors_influence=models.CharField(max_length=250)
    rating_own_phone=models.IntegerField()
    describe_your_phone=models.CharField(max_length=250)
    Mojor_concern=models.CharField(max_length=250)
    apps_security=models.IntegerField()
    ios_android=models.CharField(max_length=250)
    occupation=models.CharField(max_length=250)
class report(models.Model):
    Name=models.CharField(max_length=250)
    date=models.DateField()
    comment=models.TextField()