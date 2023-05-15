# For Pre processing
"Author: Kazi Jahidur Rahaman, HNE Eberswalde, 2023"

# Cloud masking for Surface Reflectance Products (Nill et. al., 2019)
def fctn_cloud(img):
    import ee
    
    img = ee.Image(img)
    cloudShadowBitMask = ee.Number(2).pow(3).int()
    cloudsBitMask = ee.Number(2).pow(5).int()
    snowBitMask = ee.Number(2).pow(4).int()
    qa = img.select('pixel_qa')
    mask = qa.bitwiseAnd(cloudShadowBitMask).eq(0).And(qa.bitwiseAnd(cloudsBitMask).eq(0)).And(
        qa.bitwiseAnd(snowBitMask).eq(0))
    return img.updateMask(mask)


def fctn_bndscale_ls8(img):
    import ee
    
    img = ee.Image(img)
    bands = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7']
    new_bands = ['blue', 'green', 'red', 'nir', 'swir1', 'swir2']
    visnirswir = img.select(bands).rename(new_bands)
    return visnirswir.copyProperties(img, ['system:time_start'])

#clipping
def fctn_clip(img):
    import ee
    
    img = ee.Image(img)
    clip_img = img.clip(aoi)
    return clip_img 