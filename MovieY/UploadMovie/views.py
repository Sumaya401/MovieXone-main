from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from UploadMovie.models import movieUping
# Create your views here


def UpV(request):
    return render(request, 'Upload_Movies.html')

def VideoDiplay(request):
    all_uploads = movieUping.objects.all()
    return render(request, 'MovieInfo.html', {'uploads': all_uploads})

def UploadedMovie(request):
    if request.method == 'POST' and request.FILES['videoFile']:
        videoMeta = request.FILES['videoFile']
        fs = FileSystemStorage()
        filename = fs.save(videoMeta.name, videoMeta)
        videoURL = fs.url(filename)
        New_MovieUping = movieUping(
            video=videoURL,
            movie_name=request.POST['movie_name'],
            description=request.POST['description'],
            genre=request.POST['genre'],
            release_year=request.POST['release_year'],
            video_id=request.POST['video_id'],
        )
        New_MovieUping.save()
        return redirect ('/VideoDiplay/')
    else:
        pass
        # return redirect ('main/')
