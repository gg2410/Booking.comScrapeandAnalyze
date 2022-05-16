import pandas as pd

hotels = pd.read_csv("Lab3\latlongSingapore.csv")

import plotly.express as px

fig = px.scatter_mapbox(hotels, lat="lat_p", lon="lon_p", hover_name="hotel", color_discrete_sequence=["red"], zoom=12, height=500)
fig.update_layout(mapbox_style="carto-darkmatter")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()