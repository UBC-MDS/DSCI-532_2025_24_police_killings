from dash import Dash, html
import dash_bootstrap_components as dbc
from components.title import title
from components.sidebar import sidebar
from components.footer import footer
from components.charts import two_charts
from components.tab import tab
import callbacks

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], title='Police Killings')

# Add this line for deployment compatibility
# server = app.server

# Layout
app.layout = dbc.Container([
    dbc.Row([title], className='custom-header'),
    dbc.Row([
        sidebar,
        dbc.Col([
            tab,
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col(two_charts),
            ]),
        ], md=10),
    ]),
    html.Hr(),
    dbc.Row(dbc.Col(footer))
], fluid=True)

# Run the app/dashboards
if __name__ == '__main__':
    app.run(debug=True)