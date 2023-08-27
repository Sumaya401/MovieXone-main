from django.contrib import admin
from django.urls import path
from UploadMovie.views import UpV,VideoDiplay,UploadedMovie
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UpV ),
    path('main/', UpV ),
    path('uploadedmovie/', UploadedMovie, name='uploadedmovie'),
    path('VideoDiplay/', VideoDiplay),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)