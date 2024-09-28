from django.db import models

class Legislator(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bill(models.Model):
    title = models.CharField(max_length=255)
    sponsor = models.ForeignKey(Legislator, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Vote(models.Model):
    legislator = models.ForeignKey(Legislator, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.legislator.name} - {self.vote_type} - {self.bill.title}"
