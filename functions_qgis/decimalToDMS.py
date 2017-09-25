@qgsfunction(args="auto", group='Custom')
def decimalDegrees2DMS(dd, axis, feature, parent):
  abs_dd=abs(dd)
  deg = int(abs_dd)
  min_float = ((abs_dd - deg) * 60)
  min = int(min_float)
  sec = (min_float - min) * 60
  dms=('%d°%d\'%d\"' % (deg, min, round(sec,0)))
  if dd >= 0:
    dms=(('%sN' if axis=='NS' else '%sE') % (dms))
  else:
    dms=(('%sS' if axis=='NS'  else '%sW') % (dms))
  return dms