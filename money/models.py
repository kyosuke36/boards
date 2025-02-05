from django.db import models


class Money(models.Model):
    purpose_text = models.CharField(max_length=200, default="1")
    day_text = models.CharField(max_length=200)
    money_text = models.CharField(max_length=100)

    def __str__(self):
        return self.purpose_text


class Result(models.Model):
    money = models.ForeignKey(Money, on_delete=models.CASCADE)
    age_text = models.IntegerField(default=1)
    age_nam = models.IntegerField(default=0)
    active_text = models.BooleanField(default=True)

    def __str__(self):
        return str(self.age_text)
