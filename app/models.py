from django.db import models


class User(models.Model):
    def __str__(self):
        return self.name

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    createTime = models.DateTimeField()
    enable = models.BooleanField(default=True)


class Book(models.Model):
    def __str__(self):
        return self.name
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    publishTime = models.DateTimeField()
    enable = models.BooleanField(default=True)
    user = models.ForeignKey(User, to_field='id')
