from django.db import models

# Create your models here.


class Club_Members(models.Model):
    name = models.CharField(max_length=60)
    contact1 = models.CharField(max_length=11)
    contact2 = models.CharField(max_length=11)
    address = models.TextField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'clubmembers'
        verbose_name_plural = 'Club Members'
        ordering = ['-id']


class Joma(models.Model):
    member = models.ForeignKey(
        Club_Members, on_delete=models.CASCADE)
    amount = models.IntegerField()
    kisti = models.DateField()

    def __str__(self):
        return f"ID:{self.member_id} Name: {self.member} gave {self.amount}/=Tk on {self.kisti}"

    class Meta:
        db_table = 'joma'
        verbose_name_plural = 'Joma details'
        ordering = ['-kisti']
