#installing libraries
!pip install geemap
!pip install geopandas

# loading necessary libraries
import os
import sys
import ee
import geemap
import geopandas as gpd
import pandas as pd
from tqdm import tqdm

#mounting the google dirive
from google.colab import drive
drive.mount('/content/drive')

# setting the working directory
os.chdir('/content/drive/MyDrive/GEE')
print("Current working directory: {0}".format(os.getcwd()))

# Trigger the authentication flow.
ee.Authenticate()

# Initialize the library.
ee.Initialize()

# user input
# Study period
from_year = 2013
to_year = 2021
from_month = 1
to_month = 12
maximum_cloud = 10# in percentage

# AOI
roi =  '/content/drive/MyDrive/GEE/aoi3.shp' # insert input here
aoi = geemap.shp_to_ee(roi)

# Cloud masking for Surface Reflectance Products (Nill et. al., 2019)
def fctn_cloud(img):
       cloudShadowBitMask = ee.Number(2).pow(3).int()
       cloudsBitMask = ee.Number(2).pow(5).int()
       snowBitMask = ee.Number(2).pow(4).int()
       qa = img.select('pixel_qa')
       mask = qa.bitwiseAnd(cloudShadowBitMask).eq(0).And(
              qa.bitwiseAnd(cloudsBitMask).eq(0)).And(
              qa.bitwiseAnd(snowBitMask).eq(0))
       return img.updateMask(mask)

# renaming bands
def fctn_bndscale_ls8(img):
       bands = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7']
       new_bands = ['blue', 'green', 'red', 'nir', 'swir1', 'swir2']
       visnirswir = img.select(bands).rename(new_bands)
       return visnirswir.copyProperties(img, ['system:time_start'])

#clipping
def fctn_clip(img):
  clip_img = img.clip(aoi)
  return clip_img

# NDBI
def fctn_ndbi(img):
    ndbi = img.normalizedDifference(['swir1', 'nir']).rename('NDBI')
    return img.addBands(ndbi) 
