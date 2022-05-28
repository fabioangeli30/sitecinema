import datetime
from django.db import models
# Create your models here.
RUOLI= [
    ('a', 'attore'),
    ('r', 'regista'),
    ('ar', 'attore/regista'),
    ]

class Persona(models.Model):
    name=models.CharField(max_length=250,blank=True,null=True)
    surname=models.CharField(max_length=250,blank=True,null=True)
    role=models.CharField(max_length=50,
                  choices=RUOLI,blank=True,null=True)
    nazionalita=models.CharField(max_length=50,blank=True,null=True)
    year = models.CharField(max_length=4,blank=True, null=True)

    @property
    def get_year(self):
        # format it to datetime object. You need to convert `year` to str if it is `IntergerField`. ex: str(self.year).
        date = datetime.datetime.strptime('%Y', self.year)
        return date

class Film(models.Model):
    cast= models.ManyToManyField(Persona,related_name='cast')
    code_film = models.CharField(max_length=50)
    title = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=4,blank=True, null=True)

    def __str__(self):
        return self.title
    
    @property
    def get_year(self):
        # format it to datetime object. You need to convert `year` to str if it is `IntergerField`. ex: str(self.year).
        date = datetime.datetime.strptime('%Y', self.year)
        return date

class Proiezione(models.Model):
    film= models.ForeignKey(Film, on_delete=models.CASCADE)
    date= models.DateTimeField(blank=True,null=True)
    number_spectators= models.IntegerField(blank=True,null=True)


class Cinema(models.Model):
    name=models.CharField(max_length=250,blank=True,null=True)
    url=models.URLField(blank=True,null=True)
    city=models.CharField(max_length=350,null=True,blank=True)

class Sala(models.Model):
    proiezione=models.ForeignKey(Proiezione, on_delete=models.CASCADE)
    cinema=models.ForeignKey(Cinema, on_delete=models.CASCADE)
    is_3d=models.BooleanField(default=False,blank=True,null=True)


