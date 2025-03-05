from dash import html
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

us_map = dbc.Col([
    html.H4('Police Killings Across the United States'),
    dvc.Vega(id='map', spec={})
])

race_chart = dbc.Col([
    html.Br(),
    html.H4('Race/Ethnicity Distribution of Police Killings Victims', style={"text-align": "center"}),
    dvc.Vega(id='race_bar', spec={})
])

two_charts = dvc.Vega(id='top10_time', spec={})