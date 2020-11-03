from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import redirect
from dashboard.models import Review

class ReviewsList(ListView):
    model = Review
    paginate_by = 10

class ReviewsCreate(CreateView):
    model = Review
    fields = ['number', 'game', 'release_date', 'price', 'owner', 'developer', 'publisher', 'average_playtime', 'median_playtime', 'metascore']

class ReviewsUpdate(UpdateView):
    model = Review
    fields = ['number', 'game', 'release_date', 'price', 'owner', 'developer', 'publisher', 'average_playtime', 'median_playtime', 'metascore']
    success_url = '/'

def delete(request, id):
    formObject = Review.objects.get(pk=id)
    formObject.delete()
    return redirect('dashboard:reviews-list')