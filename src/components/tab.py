from dash import html
import dash_bootstrap_components as dbc
from components.charts import us_map, race_chart

tab = dbc.Tabs([
    dbc.Tab([
        dbc.Col(us_map, md=10),
    ], label='Map'),
    dbc.Tab([
        dbc.Row([
            dbc.Col(race_chart, md=8),
        ])
    ], label='Police Killings Distribution'),
])