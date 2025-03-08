import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import html, dcc

us_map = dbc.Card([
     dbc.CardHeader(
        dbc.Col([
            dbc.Row(
                html.Label('Police Killings Across the United States by'),
                align="center"
            ),
            dbc.Row(
                dcc.Dropdown(
                    id='map_dropdown', 
                    options=[
                        {'label': 'Race/Ethnicity', 'value': 'raceethnicity'},
                        {'label': 'Age Group', 'value': 'age_group'},
                        {'label': 'Armed Status', 'value': 'armed'}
                    ],
                    value='raceethnicity',
                    clearable=False,
                    className='custom-dropdown'
                ), align="center"
            )
        ]), className='custom-card-header'
    ),
    dbc.CardBody(
        dcc.Loading(
            id='loading-1',
            type='circle',
            color='teal',
            children=[dcc.Graph(id='map')]
        ),
        className="d-flex justify-content-center align-items-center"
    )
], style={"height": "100%"})

race_chart = dbc.Card([
    dbc.CardHeader(
        dbc.Col([
            dbc.Row(
                html.Label('Distribution of Police Killings by'),
                align="center"
            ),
            dbc.Row(
                dcc.Dropdown(
                    id='bar_dropdown', 
                    options=[
                        {'label': 'Race/Ethnicity', 'value': 'raceethnicity'},
                        {'label': 'Age Group', 'value': 'age_group'},
                        {'label': 'Armed Status', 'value': 'armed'}
                    ],
                    value='raceethnicity',
                    clearable=False,
                    className='custom-dropdown'
                ), align="center"
            )
        ]), className='custom-card-header'
    ),
    dbc.CardBody(
        dcc.Loading(
            id='loading-2',
            type='circle',
            color='teal',
            children=[dvc.Vega(id='race_bar', spec={}, opt={'actions': False})]
        ),
        className="d-flex justify-content-center align-items-center"
    )
], style={"height": "100%"})

two_charts = dbc.Col([
    dbc.Card([
        dbc.CardHeader(
            dbc.Row([
                html.H5('Select the number of top states below:', className='custom-slider-title'),
                dcc.Slider(
                    id='top_state',
                    min=1, max=25, step=1,
                    value=10,
                    marks={i: {'label': str(i), 'style': {'color': 'white'}} for i in range(1, 26)},
                ),
                html.P(id='output_area')
            ], align="center"), className='custom-slider-box'
        ),
        dbc.CardBody(
            dcc.Loading(
                id='loading-3',
                type='circle',
                color='teal',
                children=[dvc.Vega(id='top10_time', spec={}, opt={'actions': False})]
            ),
            className="d-flex justify-content-center align-items-center"
        )
        ])
    ], md=12)

