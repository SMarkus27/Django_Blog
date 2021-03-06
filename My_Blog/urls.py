from django.contrib import admin
from django.urls import include, path
from post import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('blog/', views.blog, name='post-list'),
    path('create/', views.post_create, name='post-create'),
    path('post/<id>/', views.post, name='post-detail' ),
    path('post/<id>/update/', views.post_update, name='post-update' ),
    path('post/<id>/delete', views.post_delete, name='post-delete' ),
    path('search/',views.search, name='search'),
    path('tinymce/', include('tinymce.urls')),


] 

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
