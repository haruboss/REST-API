from django.db import models

# Create your models here.
class Paradigms(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)
    para = models.ForeignKey(Paradigms, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=50)
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.name