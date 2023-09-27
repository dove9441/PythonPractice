import pandas as pd
import folium
import os
import numpy as np



df = pd.read_csv('./data/parking.csv')
print("dataframe loaded.")
nparr=df.to_numpy()

newdf=df[["위도","경도"]]
newdf.to_csv('./data/Parkingloc.csv', mode='w', index=None)