from django.urls import path

from . import views


urlpatterns = [
    path('', views.poll_index.as_view(), name='poll_index'),
    path('<int:pk>/', views.poll_detail.as_view(), name='poll_detail'),
    path('<int:pk>/results/', views.results.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]