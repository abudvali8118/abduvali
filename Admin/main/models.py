from django.db import models
from django.contrib.auth.models import User
# Create your models here.

KURS = {
    ("1-kurs","1-kurs"),
    ("2-kurs","2-kurs"),
    ("3-kurs","3-kurs"),
    ("4-kurs","4-kurs")
}
class Fakultet(models.Model):
    kurs = models.CharField(choices=KURS,max_length=90,default="1-kurs")
    nomi = models.CharField(max_length=300)

    def __str__(self):
        return self.nomi
class Savollar(models.Model):
    kurs = models.CharField(choices=KURS,max_length=90,default='1-kurs')
    fakultet = models.ForeignKey(Fakultet,on_delete=models.CASCADE)
    savol = models.TextField()
    variant1 = models.CharField(null=True,blank=True,max_length=300)
    variant2 = models.CharField(null=True,blank=True,max_length=300)
    variant3 = models.CharField(null=True,blank=True,max_length=300)
    variant4 = models.CharField(null=True,blank=True,max_length=300)
    javob = models.CharField(max_length=300)
    def __str__(self):
        return self.savol
    

class Jadval(models.Model):
    kurs = models.CharField(choices=KURS,default='1-kurs',max_length=90)
    fakultet = models.ForeignKey(Fakultet,on_delete=models.CASCADE)
    ismi = models.ForeignKey(User,on_delete=models.CASCADE)
    togri_javob = models.IntegerField()
    notogri_javob = models.IntegerField()
    ball= models.IntegerField()
    timer = models.CharField(max_length=120)
    sana = models.DateField()

    def __str__(self):
        return str(self.id)