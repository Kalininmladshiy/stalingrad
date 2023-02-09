from django.contrib import admin
from django.urls import path, include
from main_page import views

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main_page')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
