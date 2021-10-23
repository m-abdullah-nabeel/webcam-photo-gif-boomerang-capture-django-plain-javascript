from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Emoji, Photo, Frame
from django.contrib.auth.decorators import login_required


def capture(request):
    if request.method == 'POST':
        print(request.POST)
        if request.POST.get('photo_captured'):
            photo=Photo()
            photo.photo_edited= request.POST.get('photo_edited')
            photo.photo_captured= request.POST.get('photo_captured')
            photo.save()
            id = photo.pk
            return redirect(show, id=id,)
    else:
        frames = Frame.objects.all()
        context = {'frames': frames,}
        return render(request,'capture.html', context)

def show(request, id):
    photo = Photo.objects.get(pk=id)
    context = {'photo': photo,}
    return render(request,'show.html', context)

def editor(request, id):
    if request.method == 'POST':
        print(request.POST)
        print(id)
        if request.POST.get('photo_edited'):
            photo = Photo.objects.get(pk=id)
            emojis = Emoji.objects.all()
            photo.photo_edited= request.POST.get('photo_edited')
            photo.save()
            context = {'photo': photo, 'emojis': emojis, }
            return render(request,'editor.html', context)
    else:
        emojis = Emoji.objects.all()
        photo = Photo.objects.get(pk=id)
        context = {'photo': photo, 'emojis': emojis, }
        return render(request,'editor.html', context)


def ListOnes(request,):
    user_id = request.user.id
    print(request.user.id)
    specifics = Photo.objects.filter(pk=user_id)
    print(len(specifics))
    return render(request, 'list.html', {'specifics': specifics, })
