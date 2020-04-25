import time

import folium
import pandas as pd
from flask import Flask

app = Flask(__name__)
dataset=pd.read_excel('covid-19.xlsx')
place = dataset[ ['Latitude', 'Longitude'] ]
place=place.values.tolist()

c_map=folium.Map(
    location=[20.5937, 78.9629],  
    zoom_start=5
)

def covid(i,color):
    folium.Marker(
        location=point,
        popup=str(dataset["Confirmed Cases"][i]),  
        icon=folium.Icon(
            color=color,
            icon='tint',
            icon_color='white'
        )
    ).add_to(c_map)
i=0
for point in place:
    if dataset['Confirmed Cases'][i]>1000:
        covid(i,'red')
    elif dataset['Confirmed Cases'][i]>500:
        covid(i,'orange')
    else:
        covid(i,'green')
    i+=1

c_map.save('index.html')

@app.route('/')

return render_template('index.html')

