import altair as alt
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

data = pd.read_csv('data/proc/clean_data.csv')
bar_chart = alt.Chart(data).mark_bar().encode(
    x = 'count()',
    y = alt.Y('raceethnicity').sort('-x'),
    color = 'gender',
    tooltip = 'count()'
).properties(
    title = 'Race/Ethnicity Distribution of Police Killings Victims'    
).interactive()

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Police Killings DashBoard'),
            html.Br(),
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Race/Ethnicity'),
            dcc.Dropdown(
                id='race', 
                options=data['raceethnicity'].unique(),
                multi=True,
                placeholder='Select multiple groups...'
                )
        ]),
        dbc.Col([
            dvc.Vega(id='map', spec={}),
            dvc.Vega(spec=bar_chart.to_dict())
            ]),
    ])
])

# Server side callbacks/reactivity
@callback(
    Output('map', 'spec'),
    Input('race', 'value')
)
def create_chart(race):
    if race is None:
        data_race = data
    else:
        data_race = data[data['raceethnicity'].isin(race)]
        data_race['raceethnicity'] = pd.Categorical(
            data_race['raceethnicity'],
            categories=race,
            ordered=True
            )

    us_map_url = "https://vega.github.io/vega-datasets/data/us-10m.json"
    us_map = alt.Chart(alt.topo_feature(us_map_url, 'states')).mark_geoshape(
        fill='lightgray', stroke='white'
    ).project(
        type='albersUsa'
    ).properties(
        title = 'Police Killings Across the United States',
        width=800,
        height=500
    )
    heatmap = alt.Chart(data_race).mark_circle(opacity=0.6, size=35).encode(
        longitude='longitude:Q',
        latitude='latitude:Q',
        # size=alt.Size('value:Q', scale=alt.Scale(range=[10, 500]), legend=None),  # Point size by value
        color=alt.Color('raceethnicity', scale=alt.Scale(scheme='category10')),
        tooltip=['latitude:Q', 'longitude:Q', 'raceethnicity']
    ).interactive()
    return (us_map + heatmap).to_dict()

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)