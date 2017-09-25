from qgis.core import *
import math

@qgsfunction(args="auto", group='Custom')
def gridToTrueNorth(geometry, feature, parent):
  #get UTM Zone at this point
  #Cheating as we're in Australia
  #We know its southern hemi and gda
  geom_pt = geometry.asPoint()

  #zone = int(math.floor(((geom_pt.x + 180) / 6) % 60) + 1)
  #utm_epsg = int(('283%d' % (zone)))
  #return utm_epsg
  utm_epsg=28355
  #Need to translate geographic GDA94 coordinate into UTM
  #TODO: Get this from project
  geo_crs = QgsCoordinateReferenceSystem()
  geo_crs.createFromId(4283, QgsCoordinateReferenceSystem.EpsgCrsId)

  #Also need the UTM CRS
  utm_crs = QgsCoordinateReferenceSystem()
  utm_crs.createFromId(utm_epsg, QgsCoordinateReferenceSystem.EpsgCrsId)

  #Transfor geographic into utm
  geo_to_utm = QgsCoordinateTransform(geo_crs, utm_crs)

  #Should check result here
  result = geometry.transform(geo_to_utm)

  #Yes invert it. we want the bearing to not from
  return -QgsBearingUtils.bearingTrueNorth(utm_crs, geometry.asPoint())