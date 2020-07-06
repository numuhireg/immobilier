import dash_html_components as html
import dash_core_components as dcc



layout = html.Div([
    html.Div([
        html.Div([
            html.H6('Répartition des biens'),
            dcc.Graph(
                id = "pieGraph",
                figure = {
                    "data": [{
                        "values": [2878001,2342181,1773296,521395],
                        "labels": [ 'Maison', 'Appartement', 'Dependance','local_indistriel' ],
                        "name": "Biens",
                        "hoverinfo":"label+name+percent",
                        "hole": .7,
                        "type": "pie",
                        "marker": {'colors':['#3b7548','#ea1313','#ffd700','#FF00FF']}
                    }],
                    "layout": {
                        "width": "2000",
                        "annotations": [{
                            "font": {
                                "size": 20
                            },
                            "showarrow": False,
                            "text": "",
                            "x": 0.2,
                            "y": 0.2
                        }],
                        "showlegend": False             
                    }
                }
            )
        ], className="six columns"),

        html.Div([
            html.H6('Effectif des biens'),

            dcc.Graph(
                id = "3",
                figure ={
                    "data": [{
                        'x':[ 'Maison', 'Appartement', 'Dependance','local_indistriel' ],
                        'y':[2878001,2342181,1773296,521395],
                        'name':'Bar biens',
                        'type':'bar',
                        'marker' :dict(color=['#3b7548','#ea1313','#ffd700','#FF00FF']),
                    }],
                    "layout": {
                        "xaxis" : dict(tickfont=dict(color='black')),
                        "yaxis" : dict(tickfont=dict(color='black')),
                        "width": "2000",
                        'yaxis':{
                            'title':'Nombre'
                        },
                        'xaxis':{
                             'title':'Type'
                        },
                        "annotations": [{
                            "font": {"size": 20},
                            "showarrow": False,
                            "text": "",
                            "x": 0.2,
                            "y": 0.2
                        }],
                        "showlegend": False                  
                    }
                }
            )

        ], className="six columns"),

    ], className="row", style={"margin": "1% 3%"})
])