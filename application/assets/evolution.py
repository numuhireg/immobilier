import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from controllers import ville

# 1. Get the data to use as dataframe
df=ville.get_ville()

#2. Set the graph into the html page
layout = html.Div([
    html.Div([
        html.Div([
            html.H6('Dix premiere departement vendus plus de biens'),
            dcc.Graph(
                id='med-graph-1',
                figure=px.line( df,x=df.Commune, y=df.counts)

#fig = 
                   
            )
        ], className="six columns"),

        html.Div([
            html.H6('Readmission'),
            dcc.Graph(
                id='med-graph-2',
                figure= px.scatter(df,x=df.Commune, y=df.counts)
                    
                
            )
        ], className="six columns"),

    ], className="row", style={"margin": "1% 3%"})
])