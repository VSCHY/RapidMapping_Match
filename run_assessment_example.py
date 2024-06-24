from src import locations
from src import assessment


######################

event = "EMSR728"

def is_flooded(in_flood):
    if in_flood == 1:
        return "flooded"
    else:
        return "not flooded"

#0: in flood shape
#1: not in flood shape but in flood postal code
#2: not at all

postalcodes = ["94315","86660", "01067"]
loc = locations(lons=[12.6, 10.7267, 13.731580522404613], 
                lats = [48.9, 48.674,51.06414796590152], 
                index = [0,1,2])

######################
assess = assessment(event)

# ON EXACT LOCATIONS
print("Exact Location")
for i in range(loc.nloc):
    point = loc.locations_gpd_4326.iloc[i]["geometry"]
    lon0 = point.x; lat0 = point.y
    in_flood = assess.exact_loc(lon0, lat0)
    print(f"*** ({i}) {is_flooded(in_flood)}")
print()
    

######################
# ON POSTAL CODE
print("From Postal Code")
for postalcode in postalcodes:
    in_flood = assess.postal_code_value(postalcode)
    print(f"*** ({i}) {postalcode} - {is_flooded(in_flood)}")
print()

# GET POSTAL CODE, on getting postal code from loc then assess
print("Get Postal Code")
for i, ind in enumerate(range(loc.nloc)):
    point = loc.locations_gpd_4326.iloc[ind]["geometry"]
    lon0 = point.x; lat0 = point.y
    postalcode = assess.get_postal_code(lon0, lat0)
    in_flood = assess.postal_code_value(postalcode)
    print(f"* ({i}) {postalcode} [true postal code: {postalcodes[i]}]", in_flood)
    