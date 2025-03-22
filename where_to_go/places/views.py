from django.shortcuts import render
from places.models import Place
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse


def index(request):
    places = list(Place.objects.all())
    geojson = {
      "type": "FeatureCollection",
      "features": []
    }
    for place in places:
        geojson['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title_short if place.title_short else '',
                    "placeId": place.id,
                    "detailsUrl": reverse('places', args=[place.id])
                }
            }
        )
    return render(request, 'index.html', {'geojson': geojson})


def places(request, id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), id=id)
    place_json = {
        'title': place.title,
        'imgs': [img.image.url for img in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }
    return JsonResponse(
        place_json,
        json_dumps_params={'indent': 5, 'ensure_ascii': False}
    )
