from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_photo/', views.add_photo, name='add_photo'),
]

urlpatterns += static(settings.ALBUM_URL, document_root=settings.ALBUM_ROOT)

