"""
test_sites.py, Sam Murphy (2017-04-20)

Creates a feature collection of Sentinel2 fileIDs (i.e. system:index), 
for tests sites which cover each of the landcover types in the 
International Geosphere Biosphere Programme (IGBP).BaseException

> test sites visualization: https://code.earthengine.google.com/a2dc973ddff3556cdfc39c8d2506a188
> for validation with synthetic data, see the original 6S_emulator repo: https://github.com/samsammurphy/6S_emulator

"""

import ee
ee.Initialize()

test_sites = ee.FeatureCollection([
  ee.Feature(ee.Geometry.Point(-10.811, 35.353),{'landcover_type':'water'}),
  ee.Feature(ee.Geometry.Point(14.2575, 60.0484),{'landcover_type':'evergreen_needleleaf_forest'}),
  ee.Feature(ee.Geometry.Point(-71.917, -10.92),{'landcover_type':'evergreen_broadleaf_forest'}),
  ee.Feature(ee.Geometry.Point(127.3975, 60.9518),{'landcover_type':'deciduous_needleleaf_forest'}),
  ee.Feature(ee.Geometry.Point(-62.0673, -24.9462),{'landcover_type':'deciduous_broadleaf_forest'}),
  ee.Feature(ee.Geometry.Point(135.7031, 46.6306),{'landcover_type':'mixed_forest'}),
  ee.Feature(ee.Geometry.Point(40.4153, 4.3889),{'landcover_type':'closed_shrubland'}),
  ee.Feature(ee.Geometry.Point(129.672, -23.695),{'landcover_type':'open_shrubland'}),
  ee.Feature(ee.Geometry.Point(25.4855, -13.1437),{'landcover_type':'woody_savanna'}),
  ee.Feature(ee.Geometry.Point(27.235, 8.429),{'landcover_type':'savanna'}),
  ee.Feature(ee.Geometry.Point(-105.59, 44.056),{'landcover_type':'grassland'}),
  ee.Feature(ee.Geometry.Point(-85.4084, 53.3596),{'landcover_type':'permanent_wetland'}),
  ee.Feature(ee.Geometry.Point(75.4239, 30.5623),{'landcover_type':'cropland'}),
  ee.Feature(ee.Geometry.Point(-99.1393, 19.4407),{'landcover_type':'urban'}),
  ee.Feature(ee.Geometry.Point(102.4915, 14.7589),{'landcover_type':'cropland_and_natural_vegetation_mosaic'}),
  ee.Feature(ee.Geometry.Point(-43.86, 67.27),{'landcover_type':'snow_and_ice'}),
  ee.Feature(ee.Geometry.Point(21.094, 25.602),{'landcover_type':'barren_or_sparsely_vegetated'})
])


"""
Use an enclosure to pass a geometry and a date range to a mapping function,
the function is used to find the fileID of the first Sentinel 2 image at
a given location (geom) and time period (start,end).
"""
def encloser(geom,start,end):
  def mapping_function(feature):
    """
    find fileIDs
    """
    
    image = ee.Image(
    ee.ImageCollection('COPERNICUS/S2')
      .filterBounds(geom)
      .filterDate(start,end)
      .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',5))
      .first()
    )
   
    properties = ee.Dictionary({
        'fileID':ee.String(img.get('system:index')),
        'date':ee.Date(img.get('system:time_start')),
        'cloud_cover':ee.Number(img.get('CLOUDY_PIXEL_PERCENTAGE')),
        'landcover_type':ee.String(feature.get('landcover_type'))
        })
    
    return ee.Feature(geom,properties)
  return mapping_function


geom = ee.Geometry.Point(-10.811, 35.353)
start = ee.Date('2000-01-01')
end = ee.Date('2020-01-01')

find_IDs = encloser(geom,start,end)

result = target_sites.map(find_IDs)