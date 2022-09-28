
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# importing rounters for restframework to work with routers  and viewsets
from rest_framework.routers import DefaultRouter
from api import views as api_view

router = DefaultRouter()
# we are registering our router to work directly with api view and models
router.register('products', api_view.ProductViewsetView, basename='product') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_site.urls')),

    # i have included the router url directly 
    path('api/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # for serving the media file to the django templates
