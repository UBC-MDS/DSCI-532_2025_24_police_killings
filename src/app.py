from dash import Dash, html
import dash_bootstrap_components as dbc
from components.title import title
from components.sidebar import sidebar
from components.footer import footer
from components.charts import two_charts
from components.tab import tab
from components.input import input_state
import callbacks

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], title='Police Killings')

# Add this line for deployment compatibility
server = app.server

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
    html.Hr(),
    dbc.Row(dbc.Col(footer))
], fluid=True)

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=False)