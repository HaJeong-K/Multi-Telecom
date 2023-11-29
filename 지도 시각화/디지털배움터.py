import pandas as pd

file_path = r'C:\Users\bean\Desktop\Multi-Telecom\a.xlsx'

df = pd.read_excel(file_path)

import pandas as pd
import folium
from folium.plugins import LocateControl
import requests

api_key = 'AIzaSyBTSWuR0vjBBxb6OMmgkaYDNCmrO517F68'


m = folium.Map(location=[37.5665, 126.9780], zoom_start=15)

for index, row in df.iterrows():
    name = row['장소명']
    address = row['주소명']
    home_page = row['상세페이지']

    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}')
    data = response.json()

    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        lat, lng = location['lat'], location['lng']

        # HTML 형식으로 하이퍼링크를 추가
        html_popup = f'<strong>{name}</strong><br>{address}<br><a href="{home_page}" target="_blank">{home_page}</a><br>'
        icon = folium.CustomIcon(icon_image=r'C:\Users\bean\Desktop\Multi-Telecom\blue_marker.png', icon_size=(60, 60))

        folium.Marker(location=[lat, lng], icon=icon, popup=folium.Popup(html_popup, max_width=300)).add_to(m)

lc = LocateControl()
lc.add_to(m)

m.save('map.html')
print(m)