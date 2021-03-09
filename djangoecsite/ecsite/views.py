from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ecsite.models import EcSite
from ecsite.serializers import EcSiteSerializer


@csrf_exempt
def ecsite_list(request):
    """
    List all ecsite, or create a new ecsite.
    """
    if request.method == 'GET':
        ecsite = EcSite.objects.all()
        serializer = EcSiteSerializer(ecsite, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EcSiteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def ecsite_detail(request, pk):
    """
    Retrieve, updata or delete a ecsite.
    """
    try:
        ecsite = EcSite.objects.get(pk=pk)
    except EcSite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EcSiteSerializer(ecsite)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EcSiteSerializer(ecsite, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ecsite.delete()
        return HttpResponse(status=204)
