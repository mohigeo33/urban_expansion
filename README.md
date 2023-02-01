<h2>Detection of Urban Area Expansion through Indices based Change Detection using Landsat Imagery in Google Earth Engine(GEE)</h2>
<br>
<p> <i>[This repository contains the codes for the titled paper.]</i></p>
<p> This study analyses built-up area expansion in Chbar Ampov, a district in Phnom Penh, Cambodia, using the Indices-based built-up index (IBI). The study used
Landsat 8 satellite images from the Google Earth Engine archive. The IBI method combines three land use indices – normalized difference built-up index (NDBI),
normalized difference vegetation index (NDVI), and modified normalized difference water index (MNDWI) - to identify urban land.</p>
<p>
  <b>Study Area</b><br>
  ![image](https://user-images.githubusercontent.com/109986838/216046284-7803e149-1222-4f1d-ae07-4e657481953f.png)


  
  <b>Dataset</b><br>
  Landsat 8 Tier 1 from Google Earth Engine Archive. (ee.ImageCollection('LANDSAT/LC08/C01/T1_SR'))
</p>
<p>
  <b>Repository Structure</b><br>
  <ul>
    <li> The file <i>'ibi_gee.py'</i> contains the code for pulling the data from GEE archive. The file also includes fuction definitions for cloud masking, and radiometric calibration, clipping for the study area and necessary functions for extracting NDBI, NDVI, MNDWI, and IBI.
      ![image](https://user-images.githubusercontent.com/109986838/216045366-f446c873-ce0d-4e10-95c8-64978e9b51b9.png)

    </li>
    <li>The file <i>'ibi_data_extraction.py'</i> contains the code for extracting NDBI, NDVI, MNDWI, and IBI from collected Landsat Imageries. First the indicies has been calculated using the functions defined in <i>'ibi_gee.py'</i> and the calculated layers has been mapped to the same dataset. Then we separate all the layers for each of the indices. For the ease of further analysis, we export the layers as GeoTIFF file to our local storage. <br>
      Then, the exported images are opened with <i>rasterio</i>. The images are are converted to binary images for <i>Builtup</i> and <i>Non-builtup</i> based on a threshold for each of the pixel values. The binary images has been exported to the local storage too. <br>
      ![image](https://user-images.githubusercontent.com/109986838/216046630-6d20f84f-19d9-4e48-b645-a4e25abf5a96.png)

      Additionally  A pandas dataframe has been generated containing corresponding pixel values for NDVI, MNDWI, NDBI, and IBI layers of 200 random points which were generated for validation, with the corresponding pixel values for further statistical analysis. The dataframe is exported to localstorage as a csv file.
      ![image](https://user-images.githubusercontent.com/109986838/216046957-cd2c1efb-8de2-46f2-971a-56b921cacce1.png)

    </li>
    <li>
      The  file <i>ibi_corr.py</i> contains the code for statistical analysises. The file uses the <i>pixelvalues_2017.csv</i> file that was generated in last step and tries to find and plot the correlation matrices between different indices 
      
    </li>
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

