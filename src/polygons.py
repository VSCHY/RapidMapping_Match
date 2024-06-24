
def filter_bounds(bounds, lon_min, lat_min, lon_max, lat_max):
    bb = bounds.copy()
    bb = bb[lon_min < bb["maxx"]]
    bb = bb[lon_max > bb["minx"]]
    bb = bb[lat_min < bb["maxy"]]
    bb = bb[lat_max > bb["miny"]] 
    return bb.index
    