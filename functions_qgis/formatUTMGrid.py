from qgis.core import *

@qgsfunction(args="auto", group='Custom')
def UTMGridMinor(grid_ref, axis, feature, parent):
  gstring=grid_ref.zfill(7) # 0 - pad
  rstr = str(gstring[-3:]) #last 3 digits
  lstr = str(gstring[:2]) #first 2 digits
  if axis == 'x':
    outstr = ('    {0}      {1}E').format(lstr, rstr)
  else:
    outstr = ('    {0}      {1}N').format(lstr, rstr)
  return outstr

