from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.template import loader
from .models import Photo
from django.conf import settings
import os

# Create your views here.
def index(request):
    photos = Photo.objects.all()
    print(settings.BASE_DIR)
    for photo in  photos:
        print("Image", photo.name, photo.image.url)
    template = loader.get_template('uploadalbum/photos.html')
    context = {'photos': photos,}
    return render(request, 'uploadalbum/photos.html', context)


def photos(request):
    print("Entered in 2")
    print(request.GET.get('id'))
    id = request.GET.get('id')
    context = {}
    albums = Album.objects.all()

    if id :
        for a in albums:
            if int(a.id) == int(id) :
                album = a
                photos = Photo.objects.all().filter(album=album)
                context = {'photos': photos,}
    template = loader.get_template('uploadalbum/photos.html')
    return render(request, 'uploadalbum/photos.html', context)


def add_photo(request):
    if request.method == 'POST' and request.FILES['Image']:
        post = request.POST
        print("File is - ",request.FILES)

        name = post['Name']
        image = request.FILES['Image']

        fs = FileSystemStorage()
        filename = fs.save(os.path.join(settings.ALBUM_ROOT, name+'.jpg'), image)
        photo = Photo(name=name, image=os.path.join('album', 'albumimages', name+'.jpg'))
        photo.save()
    return render(request, 'uploadalbum/add_photo.html')