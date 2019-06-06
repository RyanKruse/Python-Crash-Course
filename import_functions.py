def make_car(manufacturer, model, **car_info):  # 8-14
    """Builds a dictionary containing everything we know about a car."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car


def make_album(artist_name, album_title, track_count=''):  # 8-7
    """Returns a dictionary of an album's artist, title, and track count (optional)."""
    album = {'artist': artist_name.lower(), 'title': album_title.lower()}
    if track_count:
        album['tracks'] = track_count
    return album
