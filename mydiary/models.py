from django.db import models

# Create your models here.

class Author(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Entry(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author) + ' ' + str(self.pub_date)
