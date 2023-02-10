import folium
from django.shortcuts import render


VOLGOGRAD_CENTER = [48.707067, 44.516975]


def index(request):
    return render(
        request,
        'index.html',
    )


def places_map(request):
    folium_map = folium.Map(location=VOLGOGRAD_CENTER, zoom_start=11)
    site_map = folium_map._repr_html_()
    return render(request, 'map.html', context={'map': site_map})
