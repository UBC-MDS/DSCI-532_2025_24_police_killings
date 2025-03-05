from dash import html
import pandas as pd

footer = html.Div([
    html.P(
        "The Data-Driven Dashboard of Police Killings project visualizes police killings data across the United States, "
        "providing insights into trends by race, age, location, and armed status."
    ),
    html.P(
        "Contributors include Adrian Leung, Rong Wan, Tingting Chen, and Shawn Xiao Hu, "
        "as part of the UBC DSCI 532 Capstone project."
    ),
    html.P([
        "GitHub Repository: ",
        html.A(
            "Police Killings Dashboard Repo",
            href="https://github.com/UBC-MDS/DSCI-532_2025_24_police_killings",
            target="_blank"
        )
    ]),
    html.P(f"Last updated: {pd.Timestamp.today().strftime('%B %d, %Y')}"),
    ], style={'textAlign': 'center', 'fontSize': '14px', 'marginTop': '20px'})