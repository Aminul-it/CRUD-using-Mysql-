from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)
    class Meta:
        db_table = "Musician"

    def __str__(self):
        return self.first_name +" "+ self.last_name
class Album(models.Model):
    artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    relase_date = models.DateField()
    rating = (
    (1,"worst"),
    (2,"bad"),
    (3,"not bad"),
    (4,"good"),
    (5,"Excellent"),
    )
    numrs_star = models.IntegerField(choices=rating)
    class Meta:
        db_table = "Album"
    def __str__(self):
        return self.name +",Rating:"+ str(self.numrs_star)
