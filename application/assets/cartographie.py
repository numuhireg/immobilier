import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import folium
from folium import plugins
from controllers import controller


# 1. Get the locations and count
location, count = controller.get_emplacement()

# 2. Prepare the map
m = folium.Map([45, 2], zoom_start=3)
fg_1 = folium.FeatureGroup(name='markers_1').add_to(m),
plugins.MarkerCluster(location[1:100],popups = count).add_to(m),
m.save('base_map_count_bien.html')

# 3. Set the map into the html page
layout = dbc.Container([ 
	dbc.Row([
		html.Div([
			html.H1("Les biens vendus en France par ville")
		],className="row",  style={'text-align':'center', 'margin': '1% 3%'}),
		
		html.Div([
			dcc.Dropdown(
				id='bien_in',
				options=[{'label': 'Nombre de biens vendus par ville', 'value': 'emplacement_geo'}],
				value='emplacement_geo'
			)
		], className="row", style={"margin": "1% 3%"}),
		
		html.Div([
			html.Iframe(
				id='bien',
				srcDoc=open('base_map_count_bien.html').read(),
				style={
					'height':'32em',
					'width':'100%',
					'box-shadow':'4px 4px 5px',
					'background-color':'white'
				}
			)
		], className="row", style={"margin": "1% 3%"})
	])
],style={"height": "100vh"})
