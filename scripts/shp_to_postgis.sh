#!/bin/bash
process () {
   echo $1
   ogr2ogr --config SQLITE_LIST_ALL_TABLES YES -f "PostgreSQL" PG:"dbname=vic_gis active_schema=gisdata schemas=gisdata" -nlt PROMOTE_TO_MULTI -overwrite -lco SCHEMA=gisdata -lco GEOMETRY_NAME=geometry -lco SPATIAL_INDEX=YES -s_srs EPSG:4283 -a_srs EPSG:4283 $1
}

files=$(find $(pwd) -name '*.shp')
for f in $files
do
   process "$f"
done


