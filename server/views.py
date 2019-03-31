# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
import json

from .models import Word
from .models import User

def assure_connection (request):
    answer = {"answer":True}
    return JsonResponse(answer,safe=False)


def get_data(request):
    vocabulary = Word.objects.all()
    json_data = serialize("json", vocabulary)
    final_data = json.loads(json_data)
    return JsonResponse(final_data, safe=False)


def get_users(request):
    users= User.objects.all()
    json_data = serialize("json", users)
    final_data = json.loads(json_data)
    return JsonResponse(final_data, safe=False)


def insert_word(request, german_word, translation, gender):
    if Word.objects.filter(german_word=german_word.title()).exists():
        answer = german_word.title()+ " is already exists in your vocabulary"
    else:
        try:
            new_word = Word(german_word=german_word.title(), translation=translation.title(), gender=gender.title())
            new_word.save()
            answer = "Succeed"
        except ValueError:
            answer = "Failed"
    return JsonResponse(answer, safe=False)


def delete_word(request, word_id):
    answer = "Failed"
    try:
        word_deleting = Word.objects.get(pk=word_id)
        word_deleting.delete()
        answer = "Deleted: " + word_id
    except ValueError:
        answer = "Failed"
    finally:
        return JsonResponse(answer, safe=False)


def insert_user(request, user_name, password):
    answer = "before"
    try:
        new_user = User(user_name=user_name,password=password,email="fakemail@gmail.com",level=1,vocabulary="[1,2,3,4,5]")
        new_user.save()
        answer = "Succeed"
    except ValueError:
        answer ="error:"+ ValueError
    return JsonResponse(answer ,safe=False)


#        try:
#            new_user= User(user_name==user_name.title(), password=password.title())
#            new_user.save()
#            answer = "Succeed"
#        except ValueError:
#            answer = "Failed"
#        return JsonResponse(answer, safe=False)

