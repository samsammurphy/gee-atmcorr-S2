"""
testsites.py, Sam Murphy (2017-04-24)

Creates a feature collection of assetIDs for Sentinel 2 images
over tests sites that represent one of each of the landcover types 
in the International Geosphere Biosphere Programme (IGBP).

> visualize test sites:
https://code.earthengine.google.com/a2dc973ddff3556cdfc39c8d2506a188

"""

import ee
ee.Initialize()

class Testsites():
  """
  This class finds asset IDs for a collection of test sites (i.e. features)
  
  It can filter using:
    1) maximum cloud cover percentage
    2) month range (e.g. from Jan to March)
  
  returns an updated feature collection with asset ID of first valid
  image for each location, e.g. 
  assetID = 'COPERNICUS/S2/20150627T102531_20160606T223605_T31RCL'
  """
  
  def __init__(self):
    self.imageCollectionID = 'COPERNICUS/S2'
    self.startDate = ee.Date('1900-01-01')
    self.stopDate = ee.Date('2100-01-01')
    self.monthRange = (1,12)# i.e. default = whole year 
    self.maxCloudCover = 100# %
    self.sites = ee.FeatureCollection([
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


  def imageProperties(self, img):
    """
    gets properties from image (e.g. assetID, etc.) 
    """
    
    imgID = img.get('system:index')
    assetID = ee.String(self.imageCollectionID+'/').cat(ee.String(imgID))
    
    properties = ee.Dictionary({
      'assetID':assetID,
      'date':ee.Date(img.get('system:time_start')),
      'cloud_cover':ee.Number(img.get('CLOUDY_PIXEL_PERCENTAGE')),
      'valid':1
      })
    
    return properties
  
  def assetFinder(self, feature):
    """
    Finds assetIDs: will be mapped over feature collection of target sites
    """
    
    geom = feature.geometry()
    
    images = ee.ImageCollection(self.imageCollectionID)\
      .filterBounds(geom)\
      .filterDate(self.startDate,self.stopDate)\
      .filter(ee.Filter.calendarRange(self.monthRange[0],self.monthRange[1],'month'))\
      .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',self.maxCloudCover))
    
    img = ee.Image(images.first())
    
    properties = ee.Algorithms.If(img,\
      self.imageProperties(img),\
      ee.Dictionary({'assetID':'None','valid':0})\
      )
    
    updated_feature = ee.Feature(geom,properties).copyProperties(feature)
    
    return updated_feature
  
def quarter_to_monthRange(Q):
  """
  returns month range tuple for given quarter of year
  """
  monthRange = (1, 12)
  if Q:
    try:
      switch = {'Q1':(1, 3), 'Q2':(4, 6), 'Q3':(7, 9), 'Q4':(10, 12)}
      monthRange = switch[Q.upper()]
    except:
      print('Quarter not recognized!!: {}'.format(Q))
      print('using default month range...: {}'.format(monthRange))
  
  return monthRange



# USAGE
#
# # instantiate Testsites
# testsites = Testsites()

# # set attributes
# quarter = 'Q1' # i.e. quarter of year
# testsites.maxCloudCover = 10
# testsites.monthRange = quarter_to_monthRange('Q1')

# # find assets
# fc = testsites.sites.map(testsites.assetFinder)

# # check
# print(fc.getInfo())

