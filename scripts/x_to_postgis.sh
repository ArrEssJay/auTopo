#!/bin/bash

HOST='10.4.3.181'
USER='postgres'
PASSWORD='jF%H&uXRB=H4RCj{MQUDWqZJo{PoFAAuRqENHMDd)qXACj4zqa'
DBNAME='vic_gis'
ACTIVE_SCHEMA='gisdata'
SCHEMAS='gisdata'
GEOEMTRY_NAME='geometry'
IN_SRS='EPSG:4283'
OUT_SRS='EPSG:4283'

process () {
   echo $1
   ogr2ogr -f "PostgreSQL" PG:"dbname=$DBNAME active_schema=$ACTIVE_SCHEMA schemas=$SCHEMAS HOST=$HOST user=$USER password=$PASSWORD" -lco SCHEMA=$ACTIVE_SCHEMA -lco GEOMETRY_NAME=$GEOEMTRY_NAME -lco OVERWRITE=YES -nlt PROMOTE_TO_MULTI -overwrite -s_srs $IN_SRS -a_srs $OUT_SRS -nln "$2" "$1"
}

files=$(find $(pwd) -name "*.$1")
for f in $files
do
  filename=$(basename "$f")
  extension="${filename##*.}"
  filename="${filename%.*}"
  echo "$filename"
  echo "$f"
  echo "$extension"
  process "$f" "$filename"
done


