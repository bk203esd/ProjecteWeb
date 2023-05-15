from django.shortcuts import render
from scrapers.stardewWebScrapper import do_Schedule
from rest_framework.decorators import api_view, permission_classes


# Create your views here.
@api_view(['GET'])
def dbScrap(request):
    do_Schedule()
