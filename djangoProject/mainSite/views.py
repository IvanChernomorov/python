from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Songs,Artists,Albums
from django.template import loader
from .forms import ArtistsForm,AlbumsForm,SongsForm
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse


def index(request):
    songs = Songs.objects.all()
    expand_element = True
    context = {
        'songs': songs,
        'title':'Главная'
    }
    return render(request, 'main/index.html',context)

def view_ar(request):
    artists = Artists.objects.all()
    context = {
        'artists': artists,
        'title':'Посмотреть'
    }
    return render(request, 'main/view_ar.html',context)

def view_s(request):
    songs = Songs.objects.all()
    context = {
        'songs': songs,
        'title':'Посмотреть'
    }
    return render(request, 'main/view_s.html',context)

def view_al(request):
    albums = Albums.objects.all()
    context = {
        'albums': albums,
        'title':'Посмотреть'
    }
    return render(request, 'main/view_al.html',context)

def create_ar(request):
    artists = Artists.objects.all()
    error=""
    if request.method == 'POST':
        form = ArtistsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error="form is uncorrect"

    form=ArtistsForm()
    context={
        'form':form,
        'artists':artists,
        'error':error
    }
    return render(request, 'main/create_ar.html', context)

def create_al(request):
    albums = Albums.objects.all()
    error=""
    if request.method == 'POST':
        form = AlbumsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error="form is uncorrect"

    form=AlbumsForm()
    context={
        'form':form,
        'error':error,
        'albums':albums
    }
    return render(request, 'main/create_al.html',context)

def create_s(request):
    error=""
    if request.method == 'POST':
        form = SongsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error="form is uncorrect"

    form=SongsForm()
    context={
        'form':form,
        'error':error
    }
    return render(request, 'main/create_s.html',context)

def view_edit(request, id):
    template = loader.get_template('main/update.html')
    song = get_object_or_404(Songs, pk=id)
    context = {
        'song': song,
        'artists':Artists.objects.all(),
        'albums': Albums.objects.all()
    }
    if all(['id_ar' in request.POST, 'id_al' in request.POST, 'title' in request.POST, 'length' in request.POST]):
        song.id_ar = get_object_or_404(Artists, pk=request.POST['id_ar'])
        song.id_al = get_object_or_404(Albums, pk=request.POST['id_al'])
        song.title = request.POST['title']
        song.length = request.POST['length']
        song.save()
        return redirect('home')
    return HttpResponse(template.render(context, request))
