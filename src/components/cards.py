from dash import html
import dash_bootstrap_components as dbc

number_card = dbc.Card(
    html.H3(id='number', className='custom-card')
    )