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
    context = {}
    labels_avg = []
    data_avg = []

    queryset = Review.objects.order_by('-average_playtime')[:5]
    for rev in queryset:
        labels_avg.append(rev.game)
        data_avg.append(rev.average_playtime)

    labels_median = []
    data_median = []
    queryset = Review.objects.order_by('-median_playtime')[:5]
    for rev in queryset:
        labels_median.append(rev.game)
        data_median.append(rev.median_playtime)

    labels_price = []
    data_price = []
    radius_price = []
    queryset = Review.objects.order_by('-price')[:10]
    for rev in queryset:
        labels_price.append(rev.game)
        data_price.append(rev.price)
        radius_price.append(rev.metascore)

    total_reviews = Review.objects.count()
    average_iqual_zero = Review.objects.filter(average_playtime=0).count()
    average_above_zero = total_reviews - average_iqual_zero

    metascore_zero = Review.objects.filter(metascore=0).count()

    return render(request, 'dashboard.html', {
        'labels_avg': labels_avg,
        'data_avg': data_avg,
        'labels_median': labels_median,
        'data_median': data_median,
        'labels_price': labels_price,
        'data_price': data_price,
        'radius_price': radius_price,
        'total_reviews': total_reviews,
        'average_above_zero': average_above_zero,
        'metascore_zero': metascore_zero,
    })