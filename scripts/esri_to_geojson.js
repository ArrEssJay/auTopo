var arcgisToGeoJSON = require('arcgis-to-geojson-utils').arcgisToGeoJSON;
var fs = require('fs')
var path = require('path')


function traverseDir(startPath, filter) {
  if (!fs.existsSync(startPath)) {
    return;
  }
  var files = fs.readdirSync(startPath);
  for (var i = 0; i < files.length; i++) {
    var filename = path.join(startPath, files[i]);
    var stat = fs.lstatSync(filename);
    if (stat.isDirectory()) {
      traverseDir(filename, filter); //recurse
    }
    else {
      for (var f in filter){
        if (filename.indexOf(filter[f]) >= 0) {
          fileList.push(filename)
        };
      }
    }
  };
};

function processFile(filename) {
  fs.readFile(filename, 'utf8', function(err, data) {
    if (err) {
      return console.log(err);
    }
    var geojson = arcgisToGeoJSON(data);
    var gjFile = filename + '.geojson'
    fs.writeFile(gjFile, data, function(err) {
      if (err) {
        return console.log(err);
      }
      console.log("Saved: " + gjFile);
    });
  });
}

fileList=[];
traverseDir(process.cwd(), ['.esri_json','.json']);

console.log(fileList)
for (var i = 0; i < fileList.length; i++){
  console.log("Processing: "+fileList[i])
  processFile(fileList[i]);
}