import dash_bootstrap_components as dbc
from dash import dcc, html
import dash_vega_components as dvc

tab = dbc.Tabs([
    dbc.Tab([
        dvc.Vega(id='map', spec={}),
    ], label='US Map Distribution'),
    dbc.Tab([
        dvc.Vega(id='race_bar', spec={}),
    ], label='Race/Ethnicity Summary Distribution'),
])
input_state = html.Div([
        html.H5('Enter the number of top states below:'),
        dcc.Input(id='top_state', placeholder='Integer between 0 and 51', debounce=False, min=0, max=51),
        html.P(id='err', style={'color': 'red'}),
        html.P(id='output_area')
    ], style={
        'background-color': '#E4AA90',
        'padding': 9,
        }
    )
two_charts = dvc.Vega(id='top10_time', spec={})