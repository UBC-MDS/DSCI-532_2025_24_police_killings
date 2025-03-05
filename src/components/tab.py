from dash import html
import dash_bootstrap_components as dbc
from components.charts import us_map, race_chart
from components.cards import number_card

tab = dbc.Tabs([
    dbc.Tab([
        us_map,
    ], label='US Map Distribution'),
    dbc.Tab([
        dbc.Row([
            dbc.Col(race_chart),
            dbc.Col([
                html.Br(),
                number_card
            ])
        ])
    ], label='Summary Distribution'),
])