from django.db import models


class Runtext(models.Model):
    text = models.CharField(max_length=254)
    color = models.CharField(max_length=254)
    background = models.CharField(max_length=254)

    def __str__(self):
        return self.text
