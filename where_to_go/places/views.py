from django.shortcuts import render
from places.models import Place


def index(request):
    places = list(Place.objects.all().prefetch_related('images'))
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
                    "detailsUrl": {  # пока пусть будет так
                        'title': place.title,
                        'imgs': [img.image.url for img in place.images.all()],
                        'description_short': place.description_short,
                        'description_long': place.description_long,
                        'coordinates': {
                            "lng": place.longitude,
                            "lat": place.latitude
                        }
                    }
                }
            }
        )
    return render(request, 'index.html', {'geojson': geojson})
