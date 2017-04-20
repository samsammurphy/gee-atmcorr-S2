"""
test_sites.py, Sam Murphy (2017-04-20)

Define test sites that will be used to demonstrate that
the 6S emulator behaves like 6S when using some real data.

Sites were selected as one of each of the landcover types in: 
International Geosphere Biosphere Programme (IGBP)

This corresponds to the following Google Earth Engine asset:
ee.ImageCollection('MODIS/051/MCD12Q1').select('Land_Cover_Type_1')

> test sites visualization: https://code.earthengine.google.com/a2dc973ddff3556cdfc39c8d2506a188
> see the original 6S_emulator repo for validation with synthetic data: https://github.com/samsammurphy/6S_emulator

"""

import ee
ee.Initialize()

# Test sites
class Sites():
  water = ee.Feature(ee.Geometry.Point(-10.811, 35.353))
  evergreen_needleleaf_forest =  ee.Feature(ee.Geometry.Point(14.2575, 60.0484))
  evergreen_broadleaf_forest = ee.Feature(ee.Geometry.Point(-71.917, -10.92))
  deciduous_needleleaf_forest = ee.Feature(ee.Geometry.Point(127.3975, 60.9518))
  deciduous_broadleaf_forest = ee.Feature(ee.Geometry.Point(-62.0673, -24.9462))
  mixed_forest = ee.Feature(ee.Geometry.Point(135.7031, 46.6306))
  closed_shrubland = ee.Feature(ee.Geometry.Point(40.4153, 4.3889))
  open_shrubland = ee.Feature(ee.Geometry.Point(129.672, -23.695))
  woody_savanna = ee.Feature(ee.Geometry.Point(25.4855, -13.1437))
  savanna = ee.Feature(ee.Geometry.Point(27.235, 8.429))
  grassland = ee.Feature(ee.Geometry.Point(-105.59, 44.056))
  permanent_wetland = ee.Feature(ee.Geometry.Point(-85.4084, 53.3596))
  cropland = ee.Feature(ee.Geometry.Point(75.4239, 30.5623))
  urban = ee.Feature(ee.Geometry.Point(-99.1393, 19.4407))
  cropland_and_natural_vegetation_mosaic = ee.Feature(ee.Geometry.Point(102.4915, 14.7589))
  snow_and_ice = ee.Feature(ee.Geometry.Point(-43.86, 67.27))
  barren_or_sparsely_vegetated = ee.Feature(ee.Geometry.Point(21.094, 25.602))
