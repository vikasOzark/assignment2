
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# importing rounters for restframework to work with routers  and viewsets
from rest_framework.routers import DefaultRouter
from api import views as api_view

router = DefaultRouter()
router.register('products', api_view.ProductViewsetView, basename='product') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_site.urls')),
    path('api/', include(router.urls))

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # for serving the media file to the django templates
