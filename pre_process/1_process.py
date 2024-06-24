import glob
import geopandas as gpd
from shapely.geometry import box, Polygon, MultiPolygon, GeometryCollection
import geopandas as gpd
import pandas as pd
import tqdm
from shapely.ops import unary_union
import numpy as np
from src import *

######################################
import sys

EVENT = sys.argv[1]

#EVENT = "EMSR728"

######################################

g = glob.glob(f"DATA/{EVENT}/{EVENT}*/*waterExtentA*.shp")

L = []
for gg in g:
    gdf = gpd.read_file(gg)
    L.append(gdf)

combined_geometries = L[0].geometry.tolist()
for gdf in L[1:]:
    combined_geometries += gdf.geometry.tolist()

unioned_geometry = unary_union(combined_geometries)
merged_gdf = gpd.GeoDataFrame(geometry=[unioned_geometry], crs=L[0].crs)

polygons = merged_gdf["geometry"].values[0]
output = []

for poly in polygons.geoms:
    output.append(poly)

gdf_out = gpd.GeoDataFrame(geometry=output)

rdf = gpd.GeoDataFrame(pd.concat([gdf_out], ignore_index=True), crs=gdf_out.crs)
rdf.to_file(f"DATA/{EVENT}/{EVENT}.gpkg", driver="GPKG")

bounds = rdf.bounds
bounds.to_excel(f"DATA/{EVENT}/{EVENT}_bounds.xlsx", index = False)
