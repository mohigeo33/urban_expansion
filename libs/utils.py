# For misc operations
"Author: Kazi Jahidur Rahaman, HNE Eberswalde, 2023"

def fctn_downloadImageCollection(imagecollection, region, foldername):
    import os
    import ee
    from tqdm import tqdm
    import requests
    import matplotlib.pyplot as plt
    import numpy as np
    
    imagecollection = ee.ImageCollection(imagecollection)

    region = ee.FeatureCollection(region)
    
    ImageCollectionFeaturesMeta = imagecollection.getInfo()['features']
    imagecollection_size =  len(ImageCollectionFeaturesMeta) #imagecollection.size().getInfo()
    
    imagecollection_list = imagecollection.toList(imagecollection_size)
    
    for i in tqdm(range(0,imagecollection_size)):
        image = ee.Image(imagecollection_list.get(i))
        image_id = ImageCollectionFeaturesMeta[i]['id'].split('/')[-1] #image.id().getInfo()
        
        image_download_url = image.getDownloadUrl({
            'region': region.geometry().bounds().getInfo()['coordinates'], #region.geometry()
            'scale': 30,
            'format': 'GEO_TIFF'})
        
        response = requests.get(image_download_url)
        filename = "./"+str(foldername)+"/"+str(image_id)+".tiff"
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as fd:
            fd.write(response.content)        
    return



def fctn_showAllTiffsfroPath(folder_path):
    import glob
    import matplotlib.pyplot as plt
    import numpy as np
    import rasterio
    from rasterio.plot import show
    import fiona
    
    
    filenames = glob.glob(folder_path + '*.tiff')
    num_files = len(filenames)
    num_rows = (num_files + 2) // 3

    fig, axs = plt.subplots(num_rows, 3, figsize=(12, 4*num_rows))

    for idx, filename in enumerate(filenames):
        rowidx = idx // 3
        colidx = idx % 3

        Allbands = rasterio.open(filename, 'r')

        ax = axs[rowidx, colidx]
        show((Allbands, 1), ax=ax, cmap='turbo')
        ax.set_title(filename.replace('\\','/'))

        norm = plt.Normalize(vmin=Allbands.read(1).min(), vmax=Allbands.read(1).max())
        sm = plt.cm.ScalarMappable(cmap='turbo', norm=norm)
        cbar = fig.colorbar(sm, ax=ax, shrink=0.5, pad=0.05, aspect=10)
        Allbands.close()

    plt.tight_layout()
    plt.show()
    return

def convertIBItoBinary(folder_path, output_path):
    from tqdm import tqdm
    import glob
    import os
    import rasterio
    import numpy as np
    
    filepaths = glob.glob(folder_path + '*.tiff')
    num_files = len(filepaths)
    
    for i in tqdm(range(0, num_files)):
        filepath = filepaths[i].replace('\\','/')
        filename = filepath.split('/')[-1].replace('.','_Binary.')
        
        with rasterio.open(filepath) as f:
            upadated_file_data = f.read(1)
          # replace all the values less than 0
            upadated_file_data[upadated_file_data == 0] = 0
            upadated_file_data[upadated_file_data < 0.018] = -1
            upadated_file_data[upadated_file_data >= 0.018] = 1
                
                
            updatedfile_meta  = f.meta.copy()
            os.makedirs(os.path.dirname(output_path+filename), exist_ok=True)
            with rasterio.open(output_path+filename, 'w', **updatedfile_meta) as dst:
                    dst.write_band(1, upadated_file_data.astype(rasterio.int16))            
    return 