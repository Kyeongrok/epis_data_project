import webbrowser
import folium, json
import pandas as pd

m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=6)
geo_data = json.load(open('skorea_municipalities_geo_simple.json', encoding='utf-8'))

# df = pd.read_json('../../turn_farm/income_info/income_info.json', encoding='utf-8')
df = pd.read_csv('ddd.csv', encoding='utf-8', dtype={'code':'str'})
# df = df[['시군명', '총수입_금액']]
# df = df.rename(columns={'시군명':'sigun', '총수입_금액':'total_income'})
colors = ['BuGn', 'BuPu', 'GnBu', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'RdPu', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']
for color in colors:
    folium.Choropleth(geo_data=geo_data,
                      data = df,
                      columns=['sigun', 'avg_income'],
                      key_on='feature.properties.name',
                      fill_color=color,
                      fill_opacity=0.8
                      ).add_to(m)

    m.save('folium_kr{}.html'.format(color))
    webbrowser.open_new("folium_kr{}.html".format(color))