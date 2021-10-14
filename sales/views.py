from django.shortcuts import render
from django.http import HttpResponse
from common.models import Custormer
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json
# Create your views here.

def listorders(request):
    return HttpResponse("Order info is below:")

def listorders2(request):
    return HttpResponse("Order info is below2:")

def listorders3(request):
    requestbody = json.loads(request.body)
    if requestbody['action'] == 'list_customer':
        return listcustomers(request)
    elif requestbody['action'] == 'del_customer':
        return delcustomers(request)
    elif requestbody['action'] == 'add_customer':
        return addcustomers(request)
    elif requestbody['action'] == 'update_customer':
        return updatecustomers(request)
    else:
        JsonResponse({'ret': 1, 'msg': 'This request method is not supported'})


def listcustomers(request):
    # Model_name.object is the function to process this object of model
    # object.values() return all record of table, qs is the abbreviation of QuerySet, a kind of Set
    qs = Custormer.objects.values()
    retlist = list(qs)
    return JsonResponse({'ret': 0, 'retlist': retlist})

def delcustomers(request):
    request.params = json.loads(request.body)
    id = request.params['id']
    try:
        # qs = Custormer.objects.filter(id=id)
        qs = Custormer.objects.get(id=id)

    except Custormer.DoesNotExist:
        return JsonResponse({'ret': 1, 'msg': 'no record with this id'})

    qs.delete()
    return JsonResponse({'ret': 0})

def addcustomers(request):
    request.params = json.loads(request.body)
    cus_data = request.params['data']
    #create() is to insert a record to database
    record = Custormer.objects.create(name=cus_data['name'],
                             phone_number=cus_data['phone_number'],
                             address=cus_data['address'])

    return JsonResponse({'ret': 0, 'id': record.id})

def updatecustomers(request):
    request.params = json.loads(request.body)
    id = request.params['id']
    data = request.params['data']
    try:
        customer = Custormer.objects.get(id=id)
    except Custormer.DoesNotExist:
        return JsonResponse({'ret': 0,
                             'msg': 'the customer does not exist'})
    if 'name' in data:
        customer.name = data['name']
    if 'phone_number' in data:
        customer.phone_number = data['phone_number']
    if 'address' in data:
        customer.address = data['address']
    customer.save()
    return JsonResponse({'ret': 0})