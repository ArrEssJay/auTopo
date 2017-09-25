from qgis.core import *

@qgsfunction(args="auto", group='Custom')
def UTMGridMajor(grid_ref, feature, parent):
  return str(grid_ref).zfill(7)[2:4] #