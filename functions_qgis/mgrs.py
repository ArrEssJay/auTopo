from qgis.core import *
import mgrs

@qgsfunction(args="auto", group='Custom')
def getMGRSZone(lat, lon, feature, parent):
  m = mgrs.MGRS()
  return m.toMGRS(lat, lon).decode('UTF-8')