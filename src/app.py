import dash
import dash_bootstrap_components as dbc
from pages.home import layout
from utils.cache import cache
from utils.settings import DEBUG_MODE 

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], 
    assets_folder='assets',  
    title='Police Killings')

cache.init_app(
    app.server,
    config={
        'CACHE_TYPE': 'filesystem',
        'CACHE_DIR': 'tmp'
    }
)

# Deployment server setup
server = app.server  

# Set the app layout from home.py
app.layout = layout

# Run the app
if __name__ == "__main__":
    app.run_server(debug=DEBUG_MODE)
