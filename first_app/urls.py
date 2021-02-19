from django.conf.urls import url
from django.urls import path
from first_app import views
app_name  = 'practise_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('album_form',views.album_form,name='album_form'),
    path('musician_form',views.musician_form, name='musician_form'),
    path('album_list/<int:artist_id>/', views.album_list,name='album_list'),
    path('edit_musician/<int:artist_id>/',views.edit_musician, name='edit_musician'),
    path('edit_album/<int:album_id>/',views.edit_album,name='edit_album'),
    path('delete_album/<int:album_id>/',views.delete_album,name='delete_album'),
    path('delete_musician/<int:artist_id>/', views.delete_musician,name='delete_musician'),


]
