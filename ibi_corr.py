#loading libraries
import os
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics
import numpy as np
import seaborn as sns
import math
from scipy.stats import shapiro 
from scipy.stats import lognorm
from scipy.stats import kstest
from sklearn.metrics import r2_score
import altair as alt

#mounting the google dirive
from google.colab import drive
drive.mount('/content/drive')

# setting the working directory
os.chdir('/content/drive/MyDrive/GEE')
print("Current working directory: {0}".format(os.getcwd()))

####################################################################################################  Functions  ####################################################################################################
# function for loading the csv/txt file
def load_csv(filepath):
    data =  []
    col = []
    checkcol = False
    with open(filepath) as f:
        for val in f.readlines():
            val = val.replace("\n","")
            val = val.split(',')
            if checkcol is False:
                col = val
                checkcol = True
            else:
                data.append(val)
    df = pd.DataFrame(data=data, columns=col)
    return df

myData = load_csv('pixelvalues_2017.csv')
df = myData
df

# Converting the variables into numeric
#Mean
df["NDVI"] = pd.to_numeric(df["NDVI"])
df["NDBI"] = pd.to_numeric(df["NDBI"])
df["NDWI"] = pd.to_numeric(df["NDWI"])
df["IBI"] = pd.to_numeric(df["IBI"])

ndvi = df["NDVI"]
ndbi = df["NDBI"]
ndwi = df["NDWI"]
ibi = df["IBI"]

dflnv = df[(df["NDVI"] >= 0.2)]

# NDVI vs IBI
x = dflnv['NDVI']
y = dflnv['IBI']
plt.scatter(x, y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
y_hat = np.poly1d(z)(x)

plt.plot(x, y_hat, "r--", lw=1)
# text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat):0.3f}$"
# plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
#      fontsize=11, verticalalignment='top')
text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat):0.3f}$"
plt.gca().text(0.05, 0.05, text, transform=plt.gca().transAxes,
     fontsize=11, verticalalignment='bottom', horizontalalignment='left')

plt.title('NDVI vs IBI')
#plt.legend()
plt.xlabel('NDVI')
plt.ylabel('Mean IBI')

plt.figure(figsize=(15, 12))

plt.show()

dfndwi = df[(df["NDVI"] < 0.2)]

# ndwi vs LST
x = dfndwi['NDWI']
y = dfndwi['IBI']
plt.scatter(x, y)

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
y_hat = np.poly1d(z)(x)

plt.plot(x, y_hat, "r--", lw=1)
# text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat):0.3f}$"
# plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
#      fontsize=11, verticalalignment='top')
text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y,y_hat):0.3f}$"
plt.gca().text(0.95, 0.95, text, transform=plt.gca().transAxes,
     fontsize=11, verticalalignment='top', horizontalalignment='right')
plt.title('MNDWI vs IBI')
#plt.legend()
plt.xlabel('MNDWI')
plt.ylabel('IBI')

plt.figure(figsize=(15, 12))

plt.show()