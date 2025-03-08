from dash import html
import dash_bootstrap_components as dbc

title = dbc.Row([
        dbc.Col(html.H1('Police Killings in the United States', className="custom-title"))
    ], className='custom-header')