from dash import html
import dash_bootstrap_components as dbc
from components.title import title
from components.sidebar import sidebar
from components.footer import footer
from components.tab import tab
from components.input import input_state
from components.charts import two_charts
# Import the US Map component
# from pages.us_map import us_map_conponent

# Import Callbacks (Dash needs them to be registered even if they are not explicitly used in this file)
import callbacks

# ✅ Define `layout` instead of `app.layout`
layout = dbc.Container([
    # Title Row
    dbc.Row([
        dbc.Col([
            title
        ]),
    ], 
    style={
        'backgroundColor': '#D15B51',
        'padding-top': '2vh',
        'padding-bottom': '2vh',
        'min-height': '10vh',
    }),
    
    # Sidebar + Main Content
    dbc.Row([
        sidebar,
        dbc.Col([
            tab,  # Tabs for US Map & Race Distribution
            html.Br(),

            # us_map_conponent,  
            html.Br(),

            dbc.Row([
                dbc.Col([
                    dbc.Row(
                        dbc.Col([input_state], md=10)
                    ), 
                    html.Br(),
                    two_charts 
                ]),
            ]),
        ], md=10),
    ]),

    # Footer
    html.Hr(),
    dbc.Row(dbc.Col(footer))
], fluid=True) 
