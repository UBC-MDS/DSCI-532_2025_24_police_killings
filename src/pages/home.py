from dash import html
import dash_bootstrap_components as dbc
from components.title import title
from components.sidebar import sidebar
from components.footer import footer
from components.tab import tab
from components.charts import two_charts

layout = dbc.Container([
    # Title Row
    title,
    
    # Sidebar + Main Content
    dbc.Row([
        sidebar,
        dbc.Col([
            tab,
            html.Br(),
            dbc.Row(two_charts),
        ]),
    ]),

    # Footer
    html.Hr(),
    dbc.Row(dbc.Col(footer))
], fluid=True) 
