import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import html, dcc

us_map = dbc.Card([
     dbc.CardHeader(
        dbc.Row([
            dbc.Col(
                html.Div('Police Killings Across the United States by'),
                md=8
            ),
            dbc.Col(
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
                ), md=4
            )
        ], align="center", className='g-0'), 
        className='custom-card-header'
    ),
    dbc.CardBody(
        dbc.Row(
            dcc.Loading(
                id='loading-1',
                type='circle',
                color='teal',
                children=[dcc.Graph(id='map', config={'displayModeBar': False})]
            ), align='center'
        )
    )
], style={"height": "100%"})

race_chart = dbc.Card([
    dbc.CardHeader(
        dbc.Row([
            dbc.Col(
                html.Div('Distribution of Deaths by'),
                md=7
            ),
            dbc.Col(
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
                ), md=5
            )
        ], align='center', className='g-0'), 
        className='custom-card-header'
    ),
    dbc.CardBody(
        dbc.Row(
            dcc.Loading(
                id='loading-2',
                type='circle',
                color='teal',
                children=[dvc.Vega(id='race_bar', spec={}, opt={'actions': False})]
            ), align='center'
        )
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
                    className = 'custom-slider'
                ),
                html.Div('Click on each bar in the barplot to view the police killings over time in the corresponding state.')
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

