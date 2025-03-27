from django.shortcuts import render
from places.models import Place
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse


def index(request):
    places = Place.objects.all()
    geojson = {
      "type": "FeatureCollection",
      "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('places', args=[place.id])
                }
            } for place in places
      ]
    }
    return render(request, 'index.html', {'geojson': geojson})


def places(request, id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), id=id)
    place_serialize = {
        'title': place.title,
        'imgs': [img.image.url for img in place.images.all().order_by(
            'position')],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }
    return JsonResponse(
        place_serialize,
        json_dumps_params={'indent': 5, 'ensure_ascii': False}
    )
