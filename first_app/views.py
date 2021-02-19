from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Album
from first_app import forms
from django.db.models import Avg


# Create your views here.
def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'musician_list':musician_list}
    return render(request,'First_app/index.html', context=diction)
def album_list(request, artist_id):
    info_musician = Musician.objects.get(pk=artist_id)
    album_table = Album.objects.filter(artist=artist_id).order_by('name')
    rating_avg = Album.objects.filter(artist=artist_id).aggregate(Avg('numrs_star'))
    diction = {'info_musician':info_musician, 'album_table': album_table,'rating_avg':rating_avg}
    return render( request,'First_app/album_list.html', context=diction)
def musician_form(request):
    add_musician = forms.MusicianForm()
    diction = {'form':'ADD Musician','add_musician':add_musician}
    if request.method == 'POST':
        add_musician = forms.MusicianForm(request.POST)
        if add_musician.is_valid():
            add_musician.save(commit=True)
            return index(request)

    return render( request,'First_app/musician_form.html', context=diction)
def album_form(request):
    add_album = forms.AlbumForm()
    diction = {'add_album':add_album}
    if request.method == 'POST':
        add_album = forms.AlbumForm(request.POST)
        if add_album.is_valid():
            add_album.save(commit=True)
            return index(request)
    return render(request,'First_app/album_form.html', context=diction)

def edit_musician(request,artist_id):
    info_musician = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=info_musician)
    diction = {'form': form }
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST , instance=info_musician)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request,artist_id)
    return render(request, 'First_app/edit_musician.html', context=diction)
def edit_album(request,album_id):
    info_album = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=info_album)
    diction = {}
    if request.method == 'POST':
       form = forms.AlbumForm(request.POST , instance=info_album)
       if form.is_valid():
           form.save(commit=True)
           diction.update({'success_text':'SuccessFully Updated'})
    diction.update({'form1':form})
    diction.update({'album_id':album_id})
    return render(request,'First_app/edit_album.html',context=diction)
def delete_album(request,album_id):
    delete = Album.objects.get(pk=album_id).delete()
    diction = {'success_delete':'Album Successfully deleted '}
    return render(request,'First_app/delete_album.html',context=diction)
def delete_musician(request,artist_id):
    delete = Musician.objects.get(pk=artist_id).delete()
    diction = {'success_delete':'Successfully Musician Deleted'}
    return render(request,'First_app/delete_musician.html',context=diction)
