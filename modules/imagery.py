from pystac_client import Client
from shapely.geometry import Point


def fetch_image():
    api_url = "https://earth-search.aws.element84.com/v1"
    client = Client.open(api_url)
    point = Point(4.89, 52.37)

    collection = "sentinel-2-l2a" # Sentinel-2, Level 2A, Cloud Optimized GeoTiffs (COGs)

    search = client.search(
        collections=[collection],
        intersects=point,
        max_items=10,
    )

    items = search.item_collection()
    assets = items[0].assets

    print(assets["thumbnail"].href)