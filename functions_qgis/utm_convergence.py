import math
from qgis.core import *
from qgis.gui import *

@qgsfunction(args="auto", group='Custom')
def myfunc(scale_factor, centroid, feature, parent):
    #convergence (x,y) = arctan (tanh x/Ko)
    convergence =
    centroid = feature.geometry()
    longitude = centroid.asPoint().x()
    latitude = centroid.asPoint().y()
    zone_number = math.floor(((longitude + 180) / 6) % 60) + 1

    if latitude >= 0:
        zone_letter = 'N'
    else:
        zone_letter = 'S'

    return '%d%s' % (int(zone_number), zone_letter)