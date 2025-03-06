import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import html, dcc

us_map = dbc.Card([
     dbc.CardHeader('Police Killings Across the United States', className='custom-card-title'),
     dbc.CardBody(dvc.Vega(id='map', spec={}, opt={'actions': False}))
])

race_chart = dbc.Card([
    dbc.CardHeader('Race/Ethnicity Distribution of Police Killings Victims', className='custom-card-title'),
    dbc.CardBody(dvc.Vega(id='race_bar', spec={}, opt={'actions': False}))
])

two_charts = dbc.Col([
    dbc.Card([
        dbc.CardHeader(
            dbc.Row([
                html.H5('Select the number of top states below:', className='custom-slider-title'),
                dcc.Slider(
                    id='top_state',
                    min=1, max=25, step=1,
                    value=10,
                    # This will update the chart as the slider is dragged instead of only when it is released
                    # Be careful with this for functions with heavy computations as it can slow down the app
                    # updatemode='drag'
                ),
                html.P(id='output_area')
            ]), className='custom-slider-box'
        ),
        dbc.CardBody(dvc.Vega(id='top10_time', spec={}, opt={'actions': False}))
        ])
    ], md=10)