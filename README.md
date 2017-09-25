Required Python Packages:
https://github.com/cmweiss/geomag



1:25000 Topo Map of Victoria (QGIS Project)
===========================================

This project has styling for a 1:25000 topographic map of the State of Victoria.
Most useful layers as seen of state printed maps have been added and styled.

This project references layers from the state dataset (available from https://www.data.vic.gov.au/).
The layers reference a PostGIS database. Due to the size, you will need to download the referenced layers.

The required layers are checked into a separate project [here](https://github.com/RobDeBagel/vic_topo_map_sources) for convenience. However, they are not guaranteed to be current/kept updated.

Additionally, a 20m DEM hillshade layer is referenced. The 10/20m DEM data set is also freely available. `gdaldem` was used to generate the hillshade from the ArcInfo DEM. Refer to
`scripts/gdaldem_hillshade.sh`


Additional Layers
-----------------

Some additional layers useful for topo sheets have been included:
NSW/VIC Alpine Huts (nsw_vic_alpine_huts.kml) : [KOSCIUSZKO HUTS ASSOCIATION](http://www.khuts.org/)

Vic state data not available in the CC release on the 'spatial data mart':
- Electrical Transmission Network (`transmission_lines.geojson`)

Scripts
-------
Mostly just convenience wrappers around gdal/ogr tools. **TODO: Make these more useful**
- `esri-json_to_geo-json.sh` : Convert esri-style json to geojson
- `gdaldem_hillshade.sh` : Generate hillshade
- `shp_to_postgis.sh` : Recursively import shapefiles into a postgis database
- `psql_import_dem_raster.sh` : Import raster DEM into postgis database

