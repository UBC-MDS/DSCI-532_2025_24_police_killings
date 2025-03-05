import dash
import dash_bootstrap_components as dbc
from pages.home import layout
from utils.settings import DEBUG_MODE

# Import Callbacks (Necessary for Dash to recognize them)
from callbacks import charts, output, all_check  # ✅ Updated callback imports

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], title='Police Killings')

# ✅ Suppress missing component errors (for dynamic loading)
app.config.suppress_callback_exceptions = True  

# Deployment server setup
server = app.server  

# Set the app layout from home.py
app.layout = layout

# Run the app
if __name__ == '__main__':
    app.run_server(debug=DEBUG_MODE)
