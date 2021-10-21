from django.contrib import admin
from django.urls import path, include

from bboard.views import index
from bboard import urls as bboard_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bboard/', include(bboard_urls))
]
