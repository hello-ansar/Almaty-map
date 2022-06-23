# # Importing required Libraries
# # import geopandas as gpd
# import json
# import altair as alt
# import pandas as pd
#
# gdf = json.dumps('almaty.geo.json')
#
# multi = alt.selection_multi(fields=['count','state'], bind='legend')
# color = alt.condition(multi,
#                   alt.Color('count', type='ordinal',
#                   scale=alt.Scale(scheme='yellowgreenblue')),
#                   alt.value('lightgray'))
# hover = alt.selection(type='single', on='mouseover', nearest=True,
#                       fields=['x', 'y'])
#
# choro = alt.Chart(gdf).mark_geoshape(
#     stroke='black'
# ).encode(
#     color=color,
#     tooltip=['state','count']
# ).add_selection(
#         multi
#     ).properties(
#     width=650,
#     height=800
# )
#
# c1 = alt.layer(choro).configure_legend(
#     orient = 'bottom-right',
#     direction = 'horizontal',
#     padding = 10,
#     rowPadding = 15
# )
#
# labels = alt.Chart(gdf).mark_text().encode(
#     longitude='x',
#     latitude='y',
#     text='count',
#     size=alt.value(8),
#     opacity=alt.value(0.6)
# )
# c2 = alt.Chart(gdf).mark_geoshape(
#     stroke='black'
# ).encode(
#     color=color,
#     tooltip=['state','count']
# ).add_selection(
#         hover
#     ).project(
#     scale=100,
# )
# (c1+labels).configure_view(strokeWidth=0)


# from plotly.graph_objs import Scatter, Figure, Layout
# import plotly
# import plotly.graph_objs as go
# import json
# import numpy as np
#
#
#
# gdf = json.dumps('almaty.geo.json')
# with open('almaty-districts.geo.json') as response:
#     india = json.load(response)
# fig = go.Figure(go.Choroplethmapbox(geojson=india, locations=gdf['st_nm'], z=gdf['state_code'],featureidkey="properties.st_nm",colorscale="Viridis", zmin=0, zmax=25,marker_opacity=0.5, marker_line_width=1))
# fig.update_layout(mapbox_style="carto-positron",
#                   mapbox_zoom=3.5,mapbox_center = {"lat":23.537876 , "lon": 78.292142} )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()

import folium

coordinates_geo = [
    [[43.34666900, 77.01139200], "Аэропорт Алматы"],
    [[43.23157200, 76.97533900], "Канатная дорога"],
    [[43.37910100, 79.12319200], "Чарынский каньон"],
    [[43.24323300, 76.95877400], "Дворец Республики"],
    [[43.26395600, 76.93345400], "Телебашня"],
    [[43.25305600, 77.48472200], "Озеро Иссык"],
    [[43.05055600, 76.98500000], "Большое Алматинское озеро"],
    [[45.40242800, 74.15838900], "Река Или"],
    [[43.15750000, 77.05861100], "Высокогорный каток Медео"],
    [[43.28620300, 76.91095700], "Бюст Т. Шевченко"],
    [[43.16200700, 76.79512500], "Река Аксай"],
    [[43.13094700, 76.90793400], "Река Большая Алматинка"],
    [[43.34790100, 78.50425200], "Бартогай"],
    [[43.41502400, 77.58773800], "Река Тургень"],
    [[43.25861100, 76.95333300], "Вознесенский кафедральный собор"],
    [[43.26250300, 76.96864800], "Парк культуры имени М. Горького"],
    [[43.25879900, 76.95369200], "Парк имени 28 гвардейцев-панфиловцев"],
    [[43.11100900, 77.05927300], "Иле-Алатауский национальный парк"],
    [[44.33333300, 78.43333300], "Национальный парк Алтын-Эмель"],
]


# html = f"""
#     <h1> {data.iloc[i]['name']}</h1>
#     <p>You can use any html here! Let's do a list:</p>
#     <ul>
#         <li>Item 1</li>
#         <li>Item 2</li>
#     </ul>
#     </p>
#     <p>And that's a <a href="https://www.python-graph-gallery.com">link</a></p>
#     """

map = folium.Map(location=[43.2567, 76.9286], zoom_start=11)

for coordinates in coordinates_geo:
    folium.Marker(location=coordinates[0], popup=coordinates[1], icon=folium.Icon(color="gray")).add_to(map)

# folium.Marker(location=[43.23157200,76.97533900], popup="Google HQ", icon=folium.Icon(color="gray")).add_to(map)

map.save("map1.html")
