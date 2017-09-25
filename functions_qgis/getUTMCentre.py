import math
from qgis.core import *
from qgis.gui import *

def zoneMap(zone):
	zone_map = {
		1: -177,
		2: -171,
		3: -165,
		4: -159,
		5: -153,
		6: -147,
		7: -141,
		8: -135,
		9: -129,
		10: -123,
		11: -117,
		12: -111,
		13: -105,
		14: -99,
		15: -93,
		16: -87,
		17: -81,
		18: -75,
		19: -69,
		20: -63,
		21: -57,
		22: -51,
		23: -45,
		24: -39,
		25: -33,
		26: -27,
		27: -21,
		28: -15,
		29: -9,
		30: -3,
		31: 3,
		32: 9,
		33: 15,
		34: 21,
		35: 27,
		36: 33,
		37: 39,
		38: 45,
		39: 51,
		40: 57,
		41: 63,
		42: 69,
		43: 75,
		44: 81,
		45: 87,
		46: 93,
		47: 99,
		48: 105,
		49: 111,
		50: 117,
		51: 123,
		52: 129,
		53: 135,
		54: 141,
		55: 147,
		56: 153,
		57: 159,
		58: 165,
		59: 171,
		60: 177
	}
	return(zone_map.get(zone))

#return the central meridian for a UTM zone
@qgsfunction(args="auto", group='Custom')
def getUTMCentreDMS(zone, feature, parent):
	return zoneMap(zone)

def _getUTMCentreDMS(zone):
	return zoneMap(zone)

#return the central meridian for a UTM zone
@qgsfunction(args="auto", group='Custom')
def getUTMCentreUTM(zone, hemisphere,feature, parent):
	return _getUTMCentreUTM(zone, hemisphere)

def _getUTMCentreUTM(zone, hemisphere):
	meridian=zoneMap(zone)
	hemi_num = 4 if hemisphere == 'N' else 5

	zone_crs = int('32'+str(hemi_num)+str(zone))
	print("Zone CRS: "+str(zone_crs))
	crsSrc = QgsCoordinateReferenceSystem()
	crsSrc.createFromId(4326, QgsCoordinateReferenceSystem.EpsgCrsId)    # WGS 84
	crsDest = QgsCoordinateReferenceSystem()  # UTM zone
	crsDest.createFromId(zone_crs, QgsCoordinateReferenceSystem.EpsgCrsId)
	xform = QgsCoordinateTransform(crsSrc, crsDest)
	print(xform.sourceCrs())
	print(xform.destCrs())

	# forward transformation: src -> dest
	utm_meridian = xform.transform(0, meridian, direction=ForwardTransform) #use equator for lat
	print (utm_meridian)
	return utm_meridian