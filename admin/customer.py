import json
from django.http import JsonResponse
# from sales.views import listcustomers
from common.models import Custormer

def dipatcher(request):
    # assign request method to request.params
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST', 'PUT', 'DELETE']:
        request.params = json.loads(request.body)

    print("========================")
    print(request.method == 'GET')
    print(request.POST)
    print(request)
    action = request.body['action']

    if action == 'list_customer':
        return listcustomers(request)
    else: JsonResponse({'ret': 1, 'msg': 'This request method is not supported'})

def listcustomers(request):
    qs = Custormer.objects.values()
    retlist = list(qs)
    return JsonResponse({'ret': 0, 'retlist': retlist})