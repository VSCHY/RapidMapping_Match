import geopandas as gpd
import pandas as pd
import numpy as np
from src import filter_bounds

######################################
import sys

EVENT = sys.argv[1]
#EVENT = "EMSR728"

######################################

df_postal = gpd.read_file("inputs/plz-5stellig/plz-5stellig.shp")
bounds_postal = df_postal.bounds


df_b_ev = pd.read_excel( f"DATA/{EVENT}/{EVENT}_bounds.xlsx")
gdf_event = gpd.read_file(f"DATA/{EVENT}/{EVENT}.gpkg", driver="GPKG")



affected = []
for i in df_postal.index:
    minx, miny, maxx, maxy = bounds_postal.loc[i].values
    df_index = filter_bounds(df_b_ev, minx, miny, maxx, maxy)
    gdf_filtered = gdf_event.loc[df_index]
    a = gdf_filtered.intersects(df_postal.loc[i]["geometry"])
    if np.sum(a)>1:
        affected.append(i)
    else:
        b = df_postal.loc[i]["geometry"].contains(gdf_filtered)
        if b.shape[0]>0:
            affected.append(i)
            
df_postal = df_postal.loc[affected]
df_postal.to_file(f"DATA/{EVENT}/{EVENT}_Postal_code.gpkg", driver="GPKG")
df_postal.bounds.to_excel(f"DATA/{EVENT}/{EVENT}_Postal_code_bounds.xlsx", index = False)

