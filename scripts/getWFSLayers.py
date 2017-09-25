#!/usr/local/bin/python3
from owslib.wfs import WebFeatureService

#outputFormat SHAPE-ZIP

#http://services.land.vic.gov.au/geoserver_pWMS/wms?request=getCapabilities
#version 1.3
layers = [
"sii:VMVEG.PLANTATION",
"sii:VMLITE.VMLITE_BUILT_UP_AREA",
]


#http://services.land.vic.gov.au/catalogue/publicproxy/guest/dv_geoserver/wfs?request=getCapabilities
layers = [
"datavic:VMTRANS_AIRPORT_INFRASTRUCTURE",
"datavic:VMTRANS_AIRPORT_AREA_POLYGON",
"datavic:VMTRANS_AIR_INFRA_AREA_POLYGON",
"datavic:VMTRANS_TR_AIR_INFRA_POINT",

"datavic:VMTRANS_ALPS_WALKING_TRACK",
"datavic:VMTRANS_BICENTENNIAL_NATIONAL",
"datavic:VMTRANS_GREAT_DIVIDING_TRAIL",
"datavic:VMTRANS_SURF_COAST_WALK",

"datavic:VMTRANS_BIKE_BRIDGES",
"datavic:VMTRANS_TR_RAIL_BRIDGE",
"datavic:VMTRANS_TR_ROAD_BRIDGE",
"datavic:VMTRANS_TR_ROAD_FOOTBRIDGE",
"datavic:VMTRANS_TR_ROAD_FORDS",
"datavic:VMTRANS_TR_ROAD",
"datavic:VMTRANS.TR_RAIL",
"datavic:VMTRANS_TR_RAIL_INFRASTRUCTURE",
"datavic:VMTRANS_TR_FERRY_ROUTE",
"datavic:VMTRANS_GATE",
"datavic:VMTRANS_LEVEL_CROSSING",


"datavic:VMFEAT_BUILDING_POINT",
"datavic:VMFEAT_BUILDING_POLYGON",
"datavic:VMFEAT_FOI_LINE",
"datavic:VMFEAT_FOI_POLYGON",
"datavic:VMFEAT_FOI_POINT",
"datavic:VMFEAT_FOI_INDEX_CENTROID",
"datavic:VMFEAT_FOI_INDEX_EXTENT",
"datavic:VMFEAT_GNR",
datavic:VMFEAT_LOCALITY_POINT
datavic:VMFEAT_PL_PLACE_AREA_POLYGON

"datavic:CROWNLAND.PLM25",
datavic:CROWNLAND_PARKRES

"datavic:VMLITE_GEO_AREA_LABEL",
"datavic:VMLITE_GEO_POINT_LABEL",
"datavic:VMLITE_BUILT_UP_AREA",
"datavic:CATCHMENTS_LANDUSE_2014",
"datavic:VMADMIN_AD_LGA_AREA_POLYGON",
datavic:VMPROP_PARCEL_MP
datavic:VMLITE_BUILT_UP_AREA


"datavic:VMINDEX_VICMAP_MAPINDEX_SPECIAL",
"datavic:VMINDEX_VICMAP_MAPINDEX_25D",
"datavic:VMINDEX_VICMAP_MAPINDEX_25S",
"datavic:VMINDEX_VICMAP_MAPINDEX_30DA3",
"datavic:VMINDEX_VICMAP_MAPINDEX_30SA4",
"datavic:VMINDEX_VICMAP_MAPINDEX_50D",
"datavic:VMINDEX_VICMAP_MAPINDEX_50S",
"datavic:VMINDEX_VICMAP_MAPINDEX_100",D

"datavic:VMHYDRO_HY_WATERCOURSE",
"datavic:VMHYDRO_HY_WATER_POINT",
"datavic:VMHYDRO_HY_WATER_STRUCT_POINT",
datavic:VMHYDRO_HY_WATER_AREA_POLYGON
"datavic:VMHYDRO_WATER_STRUCT_CAUSEWAY",
"datavic:VMHYDRO_WATER_STRUCT_BREAKWATER",
"datavic:VMHYDRO_WATER_STRUCT_DAM_BATTER",
"datavic:VMHYDRO_WATER_STRUCT_DAM_WALL",
"datavic:VMHYDRO_WATER_STRUCT_DAM_WALL_ROAD",
"datavic:VMHYDRO_WATER_STRUCT_RAMP",
"datavic:VMHYDRO_WATER_STRUCT_LOCK",
"datavic:VMHYDRO_WATER_STRUCT_MARINA",
"datavic:VMHYDRO_WATER_STRUCT_PIPE",
"datavic:VMHYDRO_WATER_STRUCT_UG_PIPE",
"datavic:VMHYDRO_WATER_STRUCT_WATER_PLACE",
"datavic:VMHYDRO_WATER_STRUCT_WHARF",
"datavic:VMHYDRO_WATER_STRUCT_WELL",
"datavic:VMHYDRO_WATER_STRUCT_SPILLWAY",
"datavic:VMHYDRO_WATER_STRUCT_TANK",
"datavic:VMHYDRO_HY_WATER_STRUCT_AREA_TANK",

"datavic:MINERALS_SPRINGS",
"datavic:MINERALS_SITES",
"datavic:MINERALS_FACILITY",
"datavic:MINERALS_OILGAS",



"datavic:WATER_FARM_DAMS",
"datavic:WATER_FARM_DAMS_POINT",
"datavic:WATER_SPRING_LOCATIONS",

"datavic:VMINDEX_FR_FRAMEWORK_AREA_LINE",
datavic:VMINDEX_FR_FRAMEWORK_AREA_POLYGON

datavic:VMELEV_EL_GRND_TYPE_POINT,
datavic:VMELEV_EL_GRND_SURFACE_POINT
datavic:VMELEV_EL_CONTOUR
datavic:VMELEV_GROUND_TYPE_ROCK_OC
datavic:VMELEV_GROUND_TYPE_SAND,

"datavic:VMVEG_TREE_DENSITY",

]


wfs = WebFeatureService(url='http://services.land.vic.gov.au/geoserver_pWMS/sii/ows', version='1.1.0', service='WFS')
print (wfs.identification.title)

>>> wfs.identification.title
baseURL = "http://services.land.vic.gov.au/geoserver_pWMS/sii/ows"

wget "http://services.land.vic.gov.au/geoserver_pWMS/sii/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=sii:CROWNLAND.PLM25&outputFormat=shape-zip"
