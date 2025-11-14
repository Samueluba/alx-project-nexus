from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

class Customer(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

