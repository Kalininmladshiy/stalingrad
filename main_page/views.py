import folium
from django.shortcuts import render
from main_page.models import Place, Image


VOLGOGRAD_CENTER = [48.707067, 44.516975]
DEFAULT_IMAGE_URL = (
    'https://media.istockphoto.com/id/182838201/ru/%D1%84%D0%BE%D1%82%D0%BE/daisy-%'
    'D0%BD%D0%B0-%D0%B1%D0%B5%D0%BB%D0%BE%D0%BC-%D1%81-%D0%BE%D0%B1%D1'
    '%82%D1%80%D0%B0%D0%B2%D0%BA%D0%B0.jpg?s=612x612&w=0&k=20&c=R6tOX'
    'pmIYQ_LLw4H8cju_ObMFefEjJlB9p2XCPA0Z3k='
)


def add_place_on_map(folium_map, lat, lng, title, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(20, 20),
    )
    folium.Marker(
        [lng, lat],
        icon=icon,
        popup=title,
    ).add_to(folium_map)


def index(request):
    return render(
        request,
        'index.html',
    )


def places_map(request):
    folium_map = folium.Map(location=VOLGOGRAD_CENTER, zoom_start=11)
    places = Place.objects.all()

    for place in places:
        add_place_on_map(
            folium_map,
            place.lat,
            place.lng,
            place.title,
        )
    site_map = folium_map._repr_html_()
    return render(request, 'map.html', context={'map': site_map})
