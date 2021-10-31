from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Emoji, Photo, Frame
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def capture(request):
    if request.method == 'POST':
        # print(request.POST)
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
        if request.POST.get('photo_edited'):
            emojis = Emoji.objects.all()
            frames = Frame.objects.all()
            photo = Photo.objects.get(pk=id)
            photo.photo_edited= request.POST.get('photo_edited')
            photo.save()
            context = {'photo': photo, 'emojis': emojis, 'frames': frames}
            return render(request,'editor.html', context)
        else:
            frames = Frame.objects.all()
            emojis = Emoji.objects.all()
            photo = Photo.objects.get(pk=id)
            context = {'photo': photo, 'emojis': emojis, 'frames': frames}
            return render(request,'editor.html', context)
    else:
        frames = Frame.objects.all()
        emojis = Emoji.objects.all()
        photo = Photo.objects.get(pk=id)
        context = {'photo': photo, 'emojis': emojis, 'frames': frames}
        return render(request,'editor.html', context)

def ListOnes(request):
    context ={}
    context["dataset"] = Photo.objects.all().order_by('-pk')[:]
    return render(request, 'test.html', context)

def check_admin(user):
   return user.is_superuser

@login_required
@user_passes_test(check_admin)
def add_frames(request):
    if request.method == "POST":
        if request.POST.get('frame_added'):
            # print(request.POST)
            image = request.POST.get('frame_added')
            frame=Frame()
            frame.frame= request.POST.get('frame_added')
            frame.save()      
            id = frame.pk
            # print(image, id)
            return render(request, 'add_frame.html', {"id": id})
        return render(request, 'add_frame.html', )
    if request.method == "GET":
        # print("Get")
        return render(request, 'add_frame.html', )

@login_required
@user_passes_test(check_admin)
def add_images(request):
    if request.method == "POST":
        if request.POST.get('emoji_added'):
            # print(request.POST)
            image = request.POST.get('emoji_added')
            emoji=Emoji()
            emoji.emoji= request.POST.get('emoji_added')
            emoji.save()      
            id = emoji.pk
            # print(image, id)
            return render(request, 'add_emoji.html', {"id": id})
        return render(request, 'add_emoji.html', )
    if request.method == "GET":
        # print("Get")
        return render(request, 'add_emoji.html', )

