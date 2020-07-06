import dash
import dash_html_components as html
import dash_core_components as dcc
from assets import synthese, evolution, distribution, cartographie

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def config():
	server = app.server
	colors = {
		"background": "#F3F6FA", 
		"background_div": "white", 
		'text': '#009999'
	}
	app.config['suppress_callback_exceptions']= True
	app.layout = html.Div(
		style={
			'backgroundColor': colors['background']
		}, 
		children=[
	    	html.H1('Le marché immobilier en France', style={
	            'textAlign': 'center',
	            'color': colors['text']
	        }),

	      	dcc.Tabs(id="tabs", className="row", 
	      		style={
		      			"margin": "2% 3%",
		      			"height":"20",
		      			"verticalAlign":"middle"
	      			}, 
	      		value='synthese_tab', 
	      		children=[
	        		dcc.Tab(label='Vision globale synthétique', value='synthese_tab'),
	        		dcc.Tab(label='Évolution du marché immobilier', value='evolution_tab'),
	        		dcc.Tab(label='Distribution des biens sur le territoire', value='distribution_tab'),
	        		dcc.Tab(label='Localisation des biens', value='cartographie_tab')
			]),
			html.Div(id='tabs-content')
		]
	)

@app.callback(
    Output('bien', 'srcDoc'),
    [Input('bien_in', 'value')
    ])
def map(selected):
    if selected =='Nombre de biens vendus par ville':
        return open('Plugins_2 (1).html', 'r').read()

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'synthese_tab':
        return synthese.layout
    elif tab == 'evolution_tab':
        return evolution.layout
    elif tab == 'distribution_tab':
        return distribution.layout
    elif tab == 'cartographie_tab':
        return cartographie.layout
        
def main():
	config()
	app.run_server(debug=True)

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		raise e