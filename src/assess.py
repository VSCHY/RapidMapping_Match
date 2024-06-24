from .polygons import filter_bounds
import pandas as pd
import geopandas as gpd
from shapely import Point
import numpy as np



class assessment():
    def __init__(self, event):
        d_bounds = f"DATA/{event}/{event}_bounds.xlsx"
        d_shapes = f"DATA/{event}/{event}.gpkg"

        d_postal_bounds = f"DATA/{event}/{event}_Postal_code_bounds.xlsx"
        d_postal = f"DATA/{event}/{event}_Postal_code.gpkg"

        self.df_bounds = pd.read_excel(d_bounds)
        self.gdf_shapes = gpd.read_file(d_shapes)
        
        self.df_postal_bounds = pd.read_excel(d_postal_bounds)
        self.gdf_postal_shapes = gpd.read_file(d_postal)
        self.plz = list(self.gdf_postal_shapes["plz"].values)

        #
        self.postal = gpd.read_file("inputs/plz-5stellig/plz-5stellig.shp")
        self.postal_bounds = self.postal.bounds


    def exact_loc(self, lon0, lat0):
        index_loc = filter_bounds(self.df_bounds, lon0, lat0, lon0, lat0)
        gdf_filtered = self.gdf_shapes.loc[index_loc]
        gdf_filtered1 = gdf_filtered.contains(Point(lon0,lat0))
        if np.sum(gdf_filtered1.values):
            return 1
        else:
            return 0
    
    def postal_code_value(self, postalcode):
        if str(postalcode) in self.plz:
            return 1
        else:
            return 0
        
    def get_postal_code(self, lon0, lat0):
        index_loc = filter_bounds(self.postal_bounds, lon0, lat0, lon0, lat0)
        gdf_filtered = self.postal.loc[index_loc]
        gdf_filtered1 = gdf_filtered[gdf_filtered.contains(Point(lon0,lat0))]
        if gdf_filtered1.shape[0] == 0:
            print("error - no postal code")
        else:
            return gdf_filtered1["plz"].values[0]
