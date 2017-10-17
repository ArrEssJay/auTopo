<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis mincale="0" hasScaleBasedVisibilityFlag="0" version="2.99.0-Master" maxScale="0">
  <pipe>
    <rasterrenderer classificationMin="1" classificationMax="237" alphaBand="-1" type="singlebandpseudocolor" opacity="0.3" band="1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>MinMax</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader classificationMode="1" clip="0" colorRampType="INTERPOLATED">
          <colorramp name="[source]" type="gradient">
            <prop v="77,103,128,255" k="color1"/>
            <prop v="254,254,254,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.629552;160,164,139,0:0.7;168,171,140,0:0.752801;180,186,161,0" k="stops"/>
          </colorramp>
          <item label="1" value="1" color="#4d6780" alpha="255"/>
          <item label="150" value="149.574229691877" color="#a0a48b" alpha="0"/>
          <item label="166" value="166.2" color="#a8ab8c" alpha="0"/>
          <item label="179" value="178.66106442577" color="#b4baa1" alpha="0"/>
          <item label="237" value="237" color="#fefefe" alpha="255"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation saturation="0" colorizeOn="0" colorizeBlue="128" colorizeStrength="100" colorizeGreen="128" colorizeRed="255" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2" zoomedOutResampler="bilinear" zoomedInResampler="cubic"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
