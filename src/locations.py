import geopandas as gpd
import numpy as np
import pandas as pd


class locations:
    def __init__(self, lons, lats, index):
        self.L = [{ 
            "id":index, 
            "longitude":lon, 
            "latitude":lat} for idd,lon,lat in zip(np.arange(len(lons)), lons, lats)]
        locs = pd.DataFrame(self.L)        
        
        self.locations_gpd_4326 = gpd.GeoDataFrame(locs, 
                    geometry=gpd.points_from_xy(locs.longitude,locs.latitude),
                    crs = "epsg:4326")
        self.locations_gpd_3035 = self.locations_gpd_4326.to_crs("EPSG:3035")

        self.nloc = self.locations_gpd_4326.shape[0]

    def get_loc(self, radius):
        """
        radius is in meter
        """
        locations_gpd_3035_radius = self.locations_gpd_3035.copy()
        locations_gpd_3035_radius.geometry = locations_gpd_3035_radius.geometry.buffer(radius,6)
        locations_gpd_4326_radius = locations_gpd_3035_radius.to_crs("EPSG:4326")
        return locations_gpd_3035_radius, locations_gpd_4326_radius
    
    def get_proj(self, locations_in, proj):
        locations_out = locations_in.to_crs(f"EPSG:{proj}")
        return locations_out

