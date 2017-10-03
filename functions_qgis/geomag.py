from qgis.core import *

import geomag
import datetime

@qgsfunction(args="auto", group='Custom')
def getMagneticDeclination(geometry, feature, parent):
  geom_pt = geometry.asPoint()
  return geomag.declination(geom_pt.y(),geom_pt.x())

@qgsfunction(args="auto", group='Custom')
def getGeoMag1YVar(geometry, feature, parent):
  geom_pt = geometry.asPoint()
  today = datetime.datetime.now()
  y1 = today + datetime.timedelta(days=365)
  geomag_now = geomag.declination(geom_pt.y(),geom_pt.x())
  geomag_y1 = geomag.declination(geom_pt.y(),geom_pt.x(),time=y1.date())
  return geomag_y1 -geomag_now