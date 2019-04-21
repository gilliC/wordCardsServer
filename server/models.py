# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Word(models.Model):
    id = models.CharField(max_length=250,primary_key=True)
    german_word = models.CharField(max_length=250)
    translation = models.CharField(max_length=250)
    gender = models.CharField(max_length=4, default="Der")

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length = 32)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=250,blank=True)
    level = models.IntegerField()
    vocabulary = models.CharField(max_length=500,blank=True)

