# For Feature creation
"Author: Kazi Jahidur Rahaman, HNE Eberswalde, 2023"

# NDBI
def fctn_ndbi(img):
    import ee
    img = ee.Image(img)
    ndbi = img.normalizedDifference(['swir1', 'nir']).rename('NDBI')
    return img.addBands(ndbi)       

def fctn_ndwi(img):
    import ee
    img = ee.Image(img)
    ndwi = img.normalizedDifference(['green', 'swir1']).rename('NDWI')
    return img.addBands(ndwi)

# NDVI
def fctn_ndvi(img):
    import ee
    img = ee.Image(img)
    ndvi = img.normalizedDifference(['nir', 'red']).rename('NDVI')
    return img.addBands(ndvi)

# SAVI
def fctn_savi(img):
    import ee
    img = ee.Image(img)
    l = ee.Number(0.5)
    savi = img.expression('((nir - red) / (nir + red + l)) * (1+l)',{
            'nir': img.select('nir'),
            'red': img.select('red'),
            'l': l}).rename('SAVI')
    return img.addBands(savi)

def fctn_ibi(img):
    import ee
    img = ee.Image(img)
    const = ee.Number(2)
    ibi = img.expression(
        '(((const * swir1) / (swir1 + nir))-((nir / (nir + red)) + (green / (green + swir1))))   / (((const * swir1) / (swir1 + nir))+((nir / (nir + red)) + (green / (green + swir1))))',           {
            'swir1': img.select('swir1'),
            'nir': img.select('nir'),
            'red': img.select('red'),
            'green': img.select('green'),
            'const': const}).rename('IBI')
    return img.addBands(ibi)