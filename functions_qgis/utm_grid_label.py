from qgis.utils import qgsfunction
from qgis.gui import *

from qgis.core import *

@qgsfunction(args="auto", group='Custom')
def getUTMFormattedLabel(grid_number, axis, map_extent, requested_label_type, feature, parent):
  majorLabel = False
  bb = map_extent.boundingBox()
  if (grid_number  % 100000 == 0): return _UTMMajorLabel(grid_number)
  else: return _UTMMinorLabel(grid_ref)
  #else:
  #  if (axis == 'x'):
  #    return('{:0.0f} {:0.0f} {:0.0f}'.format(bb.xMinimum(),bb.xMaximum(),grid_number))
  #    if (bb.xMinimum() + 1000 > grid_number): return ('A')
  ##    if (bb.xMaximum() - 1000 < grid_number): return ('B')
  #  else:
  #    return('{:0.0f} {:0.0f} {:0.0f}'.format(bb.yMinimum(),bb.yMaximum(),grid_number))
  #    if (bb.yMinimum() + 1000 > grid_number): return ('C')
  #    if (bb.yMaximum() - 1000 < grid_number): return ('D')
  #return ('E')
  #if (majorLabel == False and requested_label_type == 'minor'):
  #  return _UTMMinorLabel(grid_number)
  #if (majorLabel == True and requested_label_type == 'major'):
  #  return _UTMMajorLabel(grid_number)
  #else: return 'X'

@qgsfunction(args="auto", group='Custom')
def UTMMinorLabel(grid_ref, feature, parent):
  return _UTMMinorLabel(grid_ref)

def _UTMMinorLabel(grid_ref):
  return "{:0.0f}".format(grid_ref)[-5:-3]

@qgsfunction(args="auto", group='Custom')
def UTMLabel(grid_ref, feature, parent):
  gstring="{:0.0f}".format(grid_ref)
  rstr = gstring[-3:]   #3 last characters
  mstr = gstring[-5:-3] #the 5th-4th characters
  #either the 1st or 1-2 for the most sig figs depending if there 6 or 7 digits
  lstr = ''
  if (len(gstring) == 6):
    lstr = gstring[0]
  elif (len(gstring) == 7):
    lstr = gstring[:2] #first 2 digits
  #return "{0}{1}{2}m{3}".format(super_scr_num(lstr),mstr,super_scr_num(rstr),'E' if axis == 'x' else 'N')
  return "{0}{1}".format(super_scr_num(lstr),mstr,)
  #return "{}-{}-{}m{}".format(lstr,mstr,rstr,'E' if axis == 'x' else 'N')

@qgsfunction(args="auto", group='Custom')
def UTMMajorLabel(grid_ref, feature, parent):
  return _UTMMajorLabel(grid_ref)

def _UTMMajorLabel(grid_ref):
  gstring="{:0.0f}".format(grid_ref)
  rstr = gstring[-3:]   #3 last characters
  mstr = gstring[-5:-3] #the 5th-4th characters
  #either the 1st or 1-2 for the most sig figs depending if there 6 or 7 digits
  lstr = ''
  axis='E'
  if (len(gstring) == 6):
    lstr = gstring[0]
  elif (len(gstring) == 7):
    axis='N'
    lstr = gstring[:2] #first 2 digits
  return "{0}{1}{2}{3}".format(super_scr_num(lstr),mstr,super_scr_num(rstr), axis)
  #return "{0}{1}{2}".format(sub_scr_num(lstr),mstr,sub_scr_num(rstr))
  #return "{}-{}-{}m{}".format(lstr,mstr,rstr,'E' if axis == 'x' else 'N')

def super_scr_num(inputText):
  """ Converts any digits in the input text into their Unicode superscript equivalent.
  Expects a single string argument, returns a string"""
  supScr = (u'\u2070',u'\u00B9',u'\u00B2',u'\u00B3',u'\u2074',u'\u2075',u'\u2076',u'\u2077',u'\u2078',u'\u2079')
  outputText = ''
  for char in inputText:
    charPos = ord(char) - 48
    if charPos <0 or charPos > 9:
      outputText += char
    else:
      outputText += supScr[charPos]
  return outputText

def sub_scr_num(inputText):
  """ Converts any digits in the input text into their Unicode subscript equivalent.
  Expects a single string argument, returns a string"""
  subScr = (u'\u2080',u'\u2081',u'\u2082',u'\u2083',u'\u2084',u'\u2085',u'\u2086',u'\u2087',u'\u2088',u'\u2089')
  outputText = ''
  for char in inputText:
    charPos = ord(char) - 48
    if charPos <0 or charPos > 9:
      outputText += char
    else:
      outputText += subScr[charPos]
  return outputText