import dash
import dash_bootstrap_components as dbc
import sys
import os

# ✅ Add src directory to system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from pages.home import layout
from utils.settings import DEBUG_MODE
import os
# Import Callbacks (Necessary for Dash to recognize them)
from callbacks import charts, filters  

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], title='Police Killings')

# Deployment server setup
server = app.server  

# Set the app layout from home.py
app.layout = layout

# Run the app
if __name__ == "__main__":
    app.run_server(debug=DEBUG_MODE, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
