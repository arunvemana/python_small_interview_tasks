from django.db import models


# Create your models here.

class UserDetails(models.Model):
    insured_name = models.CharField(max_length=250)
    insured_job = models.CharField(max_length=100)
    insured_address = models.CharField(max_length=500)
    insured_city = models.CharField(max_length=100)
    insured_state = models.CharField(max_length=100)
    insured_zip = models.IntegerField(null=True)
    insured_phone = models.CharField(max_length=150, primary_key=True)
    Created_date = models.DateField()

    def __str__(self):
        return self.insured_phone


class creationId(models.Model):
    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    trans_id = models.CharField(max_length=200)

    def __str__(self):
        return self.trans_id
