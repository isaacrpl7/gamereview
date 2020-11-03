from django.urls import path

from dashboard.views import views
from dashboard.views import reviews

urlpatterns = [
    path('', views.index, name='index'),

    #path('reviews',reviews.ReviewsList.as_view(template_name="review_list.html"), name='reviews-list'),
    path('reviews',reviews.show_page, name='reviews-list'),
    path('reviews/novo',reviews.ReviewsCreate.as_view(template_name="review_form.html"), name='reviews-add'),
    path('reviews/<int:pk>',reviews.ReviewsUpdate.as_view(template_name="review_form.html"), name='reviews-update'),
    path('reviews/excluir/<int:id>',reviews.delete, name='reviews-delete'),
]