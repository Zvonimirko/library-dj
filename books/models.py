from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=230)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title