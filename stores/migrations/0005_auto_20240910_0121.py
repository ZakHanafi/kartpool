import json
from django.db import migrations
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'data/data.json'
CITY = 'Chicago'

def load_data(apps, schema_editor):
    Store = apps.get_model('stores', 'Store')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects.get('elements', []):
            try:
                objType = obj.get('type', '')
                if objType == 'node':
                    tags = obj.get('tags', {})
                    name = tags.get('name', 'N/A')

                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    location = fromstr(f'POINT({longitude} {latitude})', srid=4326)

                    housenumber = tags.get('addr:housenumber', 'N/A')
                    street = tags.get('addr:street', 'N/A')
                    postcode = tags.get('addr:postcode', 'N/A')
                    city = tags.get('addr:city', CITY)

                    address = f"{housenumber}, {street}, {postcode}"

                    store_type = tags.get('shop', 'N/A')
                    phone = tags.get('phone', 'N/A')

                    Store(
                        name=name,
                        latitude=latitude,
                        longitude=longitude,
                        location=location,
                        store_type=store_type,
                        phone=phone[:100],
                        address=address[:100],
                        city=city
                    ).save()
            except KeyError as e:
                print(f"KeyError: {e}")

class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]

    class Meta:
        managed = False
