# from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed.')
    html = ("<h1>Главная страница</h1>\n"+
           "<p>Из первого домашнего задания про Django</p>")
    return HttpResponse(html)

def about(request):
    logger.info('About page accessed.')
    html = ("<h1>О себе</h1>\n"+
            "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel, veniam?</p>\n"+
            "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel, veniam?</p>\n"+
            "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel, veniam?</p>\n"+
            "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel, veniam?</p>\n"+
            "<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel, veniam?</p>\n"
            )

    return HttpResponse(html)


# Create your views here.
