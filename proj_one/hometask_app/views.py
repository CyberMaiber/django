# from django.shortcuts import render
from http import client
import logging
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Client, Order, GoodOne
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed.')
    return render(request,'hometask_app/base.html')

def orders_of_client(request,client_id,days_count):
    logger.info('Orders page accessed.')
    client = Client.objects.filter(pk=client_id)
    orders = Order.objects.filter(customer=client_id)\
                          .filter(date_order__date__gt=datetime.now()-timedelta(days=days_count))\
                          .order_by('date_order')
    goods_of_client = []
    for order in orders:
        for good in order.goods.filter():
            if not good in goods_of_client:
                goods_of_client.append(good)
    
    # context = {'goods':goods_of_client, 'client': client, 'lst_days':days_count}
    return render(request,'hometask_app/ordrs_clnt.html', {'goods':goods_of_client, 'client': client, 'lst_days':days_count})




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


