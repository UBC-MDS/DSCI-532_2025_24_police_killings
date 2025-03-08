from dash import html
import dash_bootstrap_components as dbc
from components.title import title
from components.sidebar import sidebar
from components.footer import footer
from components.charts import us_map, race_chart, two_charts

layout = dbc.Container([
    # Title Row
    title,
    html.Br(),
    # Sidebar + Main Content
    dbc.Row([
        sidebar,
        dbc.Col([
            dbc.Row([
                dbc.Col(
                    us_map, md=7
                ),
                dbc.Col(
                    race_chart, md=5
                )
            ], className="d-flex"),
            html.Br(),
            dbc.Row(two_charts),
        ]),
    ]),

    # Footer
    html.Hr(),
    dbc.Row(dbc.Col(footer))
], fluid=True) 
