from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
import os
from urllib.parse import urlparse
import requests
from ...models import Place, Image


class Command(BaseCommand):
    help = 'loads location from json file'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='url to json')

    def handle(self, *args, **options):
        url = options['url']

        try:
            response = requests.get(url)
            response.raise_for_status()
            response = response.json()
        except requests.exceptions.HTTPError:
            raise CommandError('error when requesting link')
        except requests.exceptions.JSONDecodeError:
            raise CommandError('invalid page format: expected JSON')

        place, created = Place.objects.get_or_create(
            title=response['title'],
            defaults={
                'short_description': response['description_short'],
                'long_description': response['description_long'],
                'longitude': response['coordinates']['lng'],
                'latitude': response['coordinates']['lat']
            }
        )
        if created:
            for number, image in enumerate(response['imgs'], start=1):
                response = requests.get(image)
                response.raise_for_status()

                name = os.path.basename(urlparse(response.url).path)
                content = ContentFile(response.content, name=name)
                Image.objects.create(
                    place=place,
                    image=content,
                    position=number
                )

            self.stdout.write(
                self.style.SUCCESS(f'Created new place: {place.title}')
            )

        else:
            raise CommandError(f'{place.title} already exists')
