from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import redirect
from django.shortcuts import render
from dashboard.models import Review
from dashboard.filters import ReviewFilter
from django.core.paginator import Paginator

def show_page(request):
    context = {}

    myFilter = ReviewFilter(
        request.GET,
        queryset=Review.objects.all()
    )
    context['myFilter'] = myFilter

    paginated_myFilter = Paginator(myFilter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginated_myFilter.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'review_list.html', context=context)

class ReviewsCreate(CreateView):
    model = Review
    fields = ['number', 'game', 'release_date', 'price', 'owners', 'developer', 'publisher', 'average_playtime', 'median_playtime', 'metascore']
    success_url = '/dashboard/reviews'

class ReviewsUpdate(UpdateView):
    model = Review
    fields = ['number', 'game', 'release_date', 'price', 'owners', 'developer', 'publisher', 'average_playtime', 'median_playtime', 'metascore']
    success_url = '/dashboard/reviews'

def delete(request, id):
    formObject = Review.objects.get(pk=id)
    formObject.delete()
    return redirect('reviews-list')