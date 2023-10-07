import streamlit as st
import pandas as pd
import numpy as np
"""Displays the locations on a map and allow the player to switch which building is selected."""
#https://discuss.streamlit.io/t/map-plotting-using-streamlit-map/765/4

### Dictionary of locations , lat+long coords, and colors 

grey="#808080"
selected="#FF0000"
#32.73056277304388, -97.10812299235272
ArlMapDict={
    'buildings' : ['Library', 'Pickard', 'Fine Arts Bridge', 'University Center', 'Planetarium', 'Engineering Research Building', 'College Park'],
    'lat' : [32.729807,  32.728938, 32.730656, 32.731573, 32.73037915564416,32.733369416850714,32.73056277304388],
    'lon' : [-97.113007, -97.111410,  -97.114563, -97.110678, -97.1121927786565,-97.11322595269705,-97.10812299235272],
    'color' : [grey,grey,grey,grey,grey,grey,grey]
}
ArlMapDF=pd.DataFrame(ArlMapDict)
option = st.selectbox("Which building?",('Library','Pickard','Fine Arts Bridge','University Center','Planetarium','Engineering Research Building','College Park'),index=None)

ChoiceIndex=ArlMapDict['buildings'].index(option)

for indice,state in enumerate(ArlMapDict['color']):
    if state != "#808080":
        ArlMapDict['color'][indice]="#808080"
    if indice==ChoiceIndex:
        ArlMapDict['color'][indice]="#FF0000"

ArlMapDF=pd.DataFrame(ArlMapDict)
st.map(ArlMapDF, latitude='lat', longitude='lon', color='color',size=10)
