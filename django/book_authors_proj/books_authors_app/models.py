from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Authors(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
