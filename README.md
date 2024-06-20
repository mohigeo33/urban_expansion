
<p>
<i>DOI: 10.1553/giscience2023_02_s18</i>
This study analyses built-up area expansion in Chbar Ampov, a district in Phnom Penh, Cambodia, using the Indices-based built-up index (IBI). The study used
Landsat 8 satellite images from the Google Earth Engine archive. The IBI method combines three land use indices – normalized difference built-up index (NDBI),
normalized difference vegetation index (NDVI), and modified normalized difference water index (MNDWI) - to identify urban land.</p>
<p>
  <b>Study Area</b><br>
  Chbar Ampov is a district in the central part of Phnom Penh, Cambodia. It was created in December 2013 by dividing eight communes from Khan Mean Chey. The district is on the east side of Phnom Penh and is separated from the city by the Bassac river. The district has an area of 86.7 square kilometres and a total population of 5280 (National Institute of Statistics, 2019).<br>
  <b>Dataset</b><br>
  Landsat 8 Tier 1 from Google Earth Engine Archive. (ee.ImageCollection('LANDSAT/LC08/C01/T1_SR'))
</p>
<p>
  <b>Repository Structure</b><br>
  <ul>
    <li> The file <i>'ibi_gee.py'</i> contains the code for pulling the data from GEE archive. The file also includes fuction definitions for cloud masking, and radiometric calibration, clipping for the study area and necessary functions for extracting NDBI, NDVI, MNDWI, and IBI.</li>
    <li>The file <i>'ibi_data_extraction.py'</i> contains the code for extracting NDBI, NDVI, MNDWI, and IBI from collected Landsat Imageries. First the indicies has been calculated using the functions defined in <i>'ibi_gee.py'</i> and the calculated layers has been mapped to the same dataset. Then we separate all the layers for each of the indices. For the ease of further analysis, we export the layers as GeoTIFF file to our local storage. <br>
      Then, the exported images are opened with <i>rasterio</i>. The images are are converted to binary images for <i>Builtup</i> and <i>Non-builtup</i> based on a threshold for each of the pixel values. The binary images has been exported to the local storage too. <br>
      Additionally  A pandas dataframe has been generated containing corresponding pixel values for NDVI, MNDWI, NDBI, and IBI layers of 200 random points which were generated for validation, with the corresponding pixel values for further statistical analysis. The dataframe is exported to localstorage as a csv file.    </li>
    <li>The  file <i>ibi_corr.py</i> contains the code for statistical analysises. The file uses the <i>pixelvalues_2017.csv</i> file that was generated in last step and tries to find and plot the correlation matrices between different indices.</li>
  </ul>
</p>
<p>
  <b>Key Packages Used</b><br>
  <ol type="i">
    <li>ee</li>
    <li>geemap</li>
    <li>pandas</li>
    <li>geopandas</li>
    <li>skimage</li>
    <li>matplotlib</li>
    <li>numpy</li>
    <li>rasterio</li>
    <li>scipy</li>
    <li>seaborn</li>
    <li>scipy</li>
    <li>sklearn</li>
    <li>tqdm</li>
    <li>requests</li>
  </ol>
</p>

<p>
  <b>Remarks</b><br>
  This repository contains only the snipets from the project. To run the code effectively, please use proper environment like Jupyter, Google Colab or Visual Studio Code. Please be noted that, the shape file for  <i>area of interest(AOI)</i> and <i>validation points</i> should be provided. 
</p>

