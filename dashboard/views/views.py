from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import Review
import csv
# Create your views here.

def index(request):
    # with open('video_games.csv') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         try:
    #             p = float(row[3])
    #             a_p = int(row[7])
    #             m_p = int(row[8])
    #             ms = int(row[9])
    #         except ValueError:
    #             p=0
    #             a_p = 0
    #             m_p = 0
    #             ms = 0
            
    #         if row[0] != 'number': #where Person_name is first column's name
    #             _, created = Review.objects.get_or_create(
    #                 number=int(row[0]),
    #                 game=row[1],
    #                 release_date=row[2],
    #                 price=p, #pode ser NA
    #                 owners=row[4],
    #                 developer=row[5],
    #                 publisher=row[6],
    #                 average_playtime=a_p, #pode ser NA
    #                 median_playtime=m_p, #pode ser NA
    #                 metascore=ms #pode ser NA
    #                 )

    return HttpResponse("VIEWS HERE")