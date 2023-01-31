#!/usr/bin/env python
# coding: utf-8

#installing libraries
# !pip install geemap
# !pip install geopandas
# !pip install earthengine-api

# !pip install Fiona

import ibi_gee

# loading necessary libraries
import os
import sys
import ee
import geemap
import geopandas as gpd
import pandas as pd
from tqdm import tqdm
import requests
from skimage.io import imread
import matplotlib.pyplot as plt

import numpy as np
import rasterio
import fiona



#just that i dont want to manipulate merge?col, i take a new variable. calculate the indices and add them to the dataset

dataset = merged_coll

dataset = dataset.map(fctn_ndbi) #NDBI
dataset = dataset.map(fctn_ndwi)  #NDWI
dataset = dataset.map(fctn_savi) #SAVI
dataset = dataset.map(fctn_ibi) #IBI
dataset = dataset.map(fctn_ndvi) #NDVI



# accumulate all the indices separatelz
allNDBI = dataset.map(lambda image: image.select('NDBI')) 
allNDWI = dataset.map(lambda image: image.select('NDWI'))
allSAVI = dataset.map(lambda image: image.select('SAVI'))
allIBI = dataset.map(lambda image: image.select('IBI'))
allNDVI = dataset.map(lambda image: image.select('NDVI'))



# downloading the raw images of indices
def fctn_downloadImage(singleimage,listtype):
    singleimage_id = singleimage.id().getInfo()

    url = singleimage.getDownloadUrl({
        'region': aoi.geometry().bounds().getInfo()['coordinates'],
        'scale': 30,
        'format': 'GEO_TIFF'
    })
    
    response = requests.get(url)
    
    filename = "./outputs/"+str(listtype)+"/"+str(singleimage_id)+".tiff"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'wb') as fd:
        fd.write(response.content)
      
    return


allNDBI_list = allNDBI.toList(allNDBI.size())

for i in tqdm(range(allNDBI.size().getInfo())):
    image = ee.Image(allNDBI_list.get(i))
    fctn_downloadImage(image,'ndbi')

    
allNDWI_list = allNDWI.toList(allNDWI.size())
for i in tqdm(range(allNDWI.size().getInfo())):
    image = ee.Image(allNDWI_list.get(i))
    fctn_downloadImage(image,'ndwi')

    
    
allSAVI_list = allSAVI.toList(allSAVI.size())
for i in tqdm(range(allSAVI.size().getInfo())):
    image = ee.Image(allSAVI_list.get(i))
    fctn_downloadImage(image,'savi')


    
allIBI_list = allIBI.toList(allIBI.size())
for i in tqdm(range(allIBI.size().getInfo())):
    image = ee.Image(allIBI_list.get(i))
    fctn_downloadImage(image,'ibi')

allNDVI_list = allNDVI.toList(allNDVI.size())
for i in tqdm(range(allNDVI.size().getInfo())):
    image = ee.Image(allNDVI_list.get(i))
    fctn_downloadImage(image,'ndvi')


#save only one image per year

#ibi yearly one image dataset
ds = allIBI
years = [year for year in range(from_year, to_year + 1)]

# Create an empty list to store the filtered collections
yearlydataset = [] #this variable contains a single image from each year


# Iterate over the years
for year in years:
    # Define the start and end dates for the current year
    start = ee.Date.fromYMD(year, 1, 1)
    end = ee.Date.fromYMD(year, 12, 31)
    
    # Filter the collection by date and select the first image
    thisyrImage = ds.filterDate(start, end).first()    
    
    # Append the filtered collection to the list
    yearlydataset.append(thisyrImage)

# Create a new collection from the list of filtered collections
yearlydataset = ee.ImageCollection.fromImages(yearlydataset)



yearlydataset_list = yearlydataset.toList(yearlydataset.size())
for i in tqdm(range(yearlydataset.size().getInfo())):
    image = ee.Image(yearlydataset_list.get(i))
    fctn_downloadImage(image,'ibi_1pryr')
    
    

#ndbi yearly one image dataset
ds = allNDBI
years = [year for year in range(from_year, to_year + 1)]

# Create an empty list to store the filtered collections
yearlydataset = [] #this variable contains a single image from each year


# Iterate over the years
for year in years:
    # Define the start and end dates for the current year
    start = ee.Date.fromYMD(year, 1, 1)
    end = ee.Date.fromYMD(year, 12, 31)
    
    # Filter the collection by date and select the first image
    thisyrImage = ds.filterDate(start, end).first()    
    
    # Append the filtered collection to the list
    yearlydataset.append(thisyrImage)

# Create a new collection from the list of filtered collections
yearlydataset = ee.ImageCollection.fromImages(yearlydataset)



yearlydataset_list = yearlydataset.toList(yearlydataset.size())
for i in tqdm(range(yearlydataset.size().getInfo())):
    image = ee.Image(yearlydataset_list.get(i))
    fctn_downloadImage(image,'ndbi_1pryr')  
    
    
    

#ndvi yearly one image dataset
ds = allNDVI
years = [year for year in range(from_year, to_year + 1)]

# Create an empty list to store the filtered collections
yearlydataset = [] #this variable contains a single image from each year


# Iterate over the years
for year in years:
    # Define the start and end dates for the current year
    start = ee.Date.fromYMD(year, 1, 1)
    end = ee.Date.fromYMD(year, 12, 31)
    
    # Filter the collection by date and select the first image
    thisyrImage = ds.filterDate(start, end).first()    
    
    # Append the filtered collection to the list
    yearlydataset.append(thisyrImage)

# Create a new collection from the list of filtered collections
yearlydataset = ee.ImageCollection.fromImages(yearlydataset)



yearlydataset_list = yearlydataset.toList(yearlydataset.size())
for i in tqdm(range(yearlydataset.size().getInfo())):
    image = ee.Image(yearlydataset_list.get(i))
    fctn_downloadImage(image,'ndvi_1pryr')

    
    
#ndwi yearly one image dataset
ds = allNDWI
years = [year for year in range(from_year, to_year + 1)]

# Create an empty list to store the filtered collections
yearlydataset = [] #this variable contains a single image from each year


# Iterate over the years
for year in years:
    # Define the start and end dates for the current year
    start = ee.Date.fromYMD(year, 1, 1)
    end = ee.Date.fromYMD(year, 12, 31)
    
    # Filter the collection by date and select the first image
    thisyrImage = ds.filterDate(start, end).first()    
    
    # Append the filtered collection to the list
    yearlydataset.append(thisyrImage)

# Create a new collection from the list of filtered collections
yearlydataset = ee.ImageCollection.fromImages(yearlydataset)



yearlydataset_list = yearlydataset.toList(yearlydataset.size())
for i in tqdm(range(yearlydataset.size().getInfo())):
    image = ee.Image(yearlydataset_list.get(i))
    fctn_downloadImage(image,'ndwi_1pryr')
    


# to show all the images
# Set the path to the folder containing the tiff files
folder_path = './outputs/ibi/'

# Load all tiff files in the folder
images = []

cmap = ['red', 'green']
for filename in os.listdir(folder_path):
    if filename.endswith('.tiff'):
        file_path = os.path.join(folder_path, filename)
        
#         Read a tif in python and Visualize the image
        firstndbi = imread(file_path)
        plt.figure(figsize=(10, 10))
        plt.imshow(firstndbi, cmap='Spectral', interpolation='nearest')
        plt.axis()

plt.colorbar()
plt.show()


# convert to binary and save the binary as tiff

from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
# Load all tiff files in the folder
images = []
outpath = './outputs/ibi/bin/'

for filename in os.listdir(folder_path):
    if filename.endswith('.tiff'):
        file_path = os.path.join(folder_path, filename)
        
#Read a tif in python and Visualize the image
        with rasterio.open(file_path) as f:
            data = f.read()
            
            bands = [] 
            for i in range(1):
                band = data[i]
                # replace all the values less than 0
                band[band == 0] = 0
                band[band < 0.018] = -1
                band[band >= 0.018] = 1
                bands.append(band_equalized)
                
                
                kwargs = f.meta.copy()
                kwargs.update({
                    'driver':'GTiff',
                    'width':f.shape[1],
                    'height':f.shape[0],
        #                 'dtype':'float64',
                    'crs':f.crs, 
                    'dtype':rasterio.float32,
                    'count':1,
                    'compress':'lzw',
                    'transform':f.transform
                })

                with rasterio.open(os.path.join(outpath, filename), 'w', **kwargs) as dst:
                    dst.write_band(1, band.astype(rasterio.float32))            


# creating a dataframe for validation points in the 'points.shp' shape file, with the pixel values in the original index image . (not the binary image)

pixeldatafarame = pd.DataFrame(columns=['PointID','NDBI','NDWI','IBI','NDVI'])
pixeldatafarame


from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

# Load all tiff files in the folder
rasterfile_ibi = './outputs/ibi_1pryr/LC08_126052_20171206.tiff'
rasterfile_ndbi = './outputs/ndbi_1pryr/LC08_126052_20171206.tiff'
rasterfile_ndwi = './outputs/ndwi_1pryr/LC08_126052_20171206.tiff'
rasterfile_ndvi = './outputs/ndvi_1pryr/LC08_126052_20171206.tiff'


shpfile = './ValPointswithxy/points2.shp'
# Load the shapefile
points = gpd.read_file(shpfile)


# Load the raster file 

#ibi
with rasterio.open(rasterfile_ibi) as src:
    file_data_ibi = src.read(1)
    transform_ibi = src.transform
    
# ndbi
with rasterio.open(rasterfile_ndbi) as src:
    file_data_ndbi = src.read(1)
    transform_ndbi = src.transform
    
#ndvi
with rasterio.open(rasterfile_ndvi) as src:
    file_data_ndvi = src.read(1)
    transform_ndvi = src.transform
    
#ndwi
with rasterio.open(rasterfile_ndwi) as src:
    file_data_ndwi = src.read(1)
    transform_ndwi = src.transform

# Get the pixel values for each point
pixel_values = []

for i, point in points.iterrows():
    
    row_ibi, col_ibi = rasterio.transform.rowcol(transform_ibi, point.geometry.x, point.geometry.y)
    pixel_value_ibi = file_data_ibi[row_ibi, col_ibi]

    
    row_ndbi, col_ndbi = rasterio.transform.rowcol(transform_ndbi, point.geometry.x, point.geometry.y)
    pixel_value_ndbi = file_data_ndbi[row_ndbi, col_ndbi]
    
    row_ndvi, col_ndvi = rasterio.transform.rowcol(transform_ndvi, point.geometry.x, point.geometry.y)
    pixel_value_ndvi = file_data_ndvi[row_ndvi, col_ndvi]
    
    row_ndwi, col_ndwi = rasterio.transform.rowcol(transform_ndwi, point.geometry.x, point.geometry.y)
    pixel_value_ndwi = file_data_ndwi[row_ndwi, col_ndwi]
    
    
    
    pixeldatafarame = pixeldatafarame.append({
        'PointID': int(point.rand_point), 
        'IBI':  pixel_value_ibi,
        'NDBI': pixel_value_ndbi,
        'NDWI': pixel_value_ndwi,
        'NDVI': pixel_value_ndvi      
    },
        ignore_index=True)



#saving the dataframe in local drive as a csv for statistical analysis
os.makedirs('outputs/2017_allindex_csv', exist_ok=True)  
pixeldatafarame.to_csv('outputs/2017_allindex_csv/pixelvalues_2017.csv') 

