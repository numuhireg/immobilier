import dash_html_components as html
import dash_core_components as dcc
from controllers import analyse
import plotly.express as px

# 1. Get the data to use as dataframe
df=analyse.get_annee()

layout = html.Div([
    html.Div([
        html.Div([
            html.H6('Evolution du marche selon les annee'),
            dcc.Graph(
                id='med-graph-1',
                figure= px.line( df,x=df.Dateformat, y=df.Valeur_fonciere)
                    
            )
        ], className="six columns"),

        html.Div([
            html.H6('Readmission'),
            dcc.Graph(
                id='med-graph-2',
                figure={
                    'data': [

                    ],
                    'layout': {
                        'title': 'Graph-2'
                    }
                }
            )
        ], className="six columns"),

    ], className="row", style={"margin": "1% 3%"})
])