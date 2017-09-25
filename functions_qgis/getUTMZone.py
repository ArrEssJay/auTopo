import math
from qgis.core import *
from qgis.gui import *

@qgsfunction(args="auto", group='Custom')
def getUTMZone(geometry, feature, parent):
    #centroid = feature.geometry()
    centroid = geometry
    longitude = centroid.asPoint().x()
    latitude = centroid.asPoint().y()
    zone_number = math.floor(((longitude + 180) / 6) % 60) + 1

    if latitude >= 0:
        zone_letter = 'N'
    else:
        zone_letter = 'S'

    return '%d%s' % (int(zone_number), zone_letter)