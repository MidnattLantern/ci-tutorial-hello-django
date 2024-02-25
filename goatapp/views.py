from django.shortcuts import render, HttpResponse


def say_goaty(request):
    return HttpResponse("goaty")