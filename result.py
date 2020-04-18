from glob import glob
import numpy as np
import folium
from folium import plugins
from folium.plugins import HeatMap
import os
import pandas as pd

show_map = os.path.join('regards.json')
show_data = os.path.join('input_file_v1_dashboard.csv')

file_data = pd.read_csv(show_data)


data = (
    np.random.normal(size=(10, 1)) *
    np.array([[0, 0, 0]]) +
    np.array([[18.908225, 72.814985, 2]])
).tolist()
m = folium.Map([18.908225, 72.814985], zoom_start=6)

HeatMap(data).add_to(folium.FeatureGroup(name='Heat Map').add_to(m))
folium.LayerControl().add_to(m)

m.save(" my.html " ) 
