from math import cos, asin, sqrt, pi


#  Haversine distance formula (returns KM)
def haversine_distance(lat1, lon1, lat2, lon2):
    p = pi / 180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))


def to_mi(km):
    return km * 0.62137
