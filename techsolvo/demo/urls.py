from django.urls import path

from . import views

urlpatterns = [

	path('song/',views.SongAPI.as_view(),name = 'song'),
	path('song/<str:gettype>/<str:pk>',views.SongAPI.as_view(),name = 'songCrud'),
	path('song/<str:gettype>',views.SongAPI.as_view(),name = 'getSong'),

]