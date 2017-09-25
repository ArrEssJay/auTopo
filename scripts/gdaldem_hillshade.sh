#!/bin/bash
process () {
  OUTFILE=$(dirname $1)/hillshade.tif
  echo $1 '->' $OUTFILE
  gdaldem hillshade $1 $OUTFILE -compute_edges -combined
}


files=$(find $(pwd) -name 'prj.adf')
for f in $files
do
   process "$f"
done




