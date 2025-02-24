import altair as alt
from dash import Dash, html, dcc, Input, Output, callback_context, callback
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

data = pd.read_csv('data/proc/clean_data.csv')

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
            html.Label('Year'),
            dcc.RadioItems(
                id='year',
                options=[2015, 2016, '2015 & 2016'], 
                value='2015 & 2016'
                ),
            html.Br(),

            html.Label('Race/Ethnicity'),
            dcc.Checklist(["All"], ["All"], id="all-checklist", inline=True),
            dcc.Checklist(
                id='race-checklist', 
                options=['Black', 'White', 'Hispanic/Latino', 
                         'Asian/Pacific Islander', 'Native American', 
                         'Arab-American', 'Other'],
                # multi=True,
                # placeholder='Select multiple groups...'
                )
        ]),
        dbc.Col([
            dvc.Vega(id='map', spec={}),
            html.Br(),
            dvc.Vega(id='race_bar', spec={}),
            # dbc.Row([
            #     dvc.Vega(id='race_bar', spec={}),
            #     dvc.Vega(id='top10_bar', spec={}),
            # ])
        ]),
    ])
])

# Server side callbacks/reactivity
@callback(
    Output('map', 'spec'),
    Input('year', 'value'),
    Input('race-checklist', 'value')
)
def create_map(year, race):
    data_filtered = data.copy()
    if year != '2015 & 2016':
        data_filtered = data_filtered[data_filtered['year'] == year]
    if race is not None:
        data_filtered = data_filtered[data_filtered['raceethnicity'].isin(race)]
        data_filtered['raceethnicity'] = pd.Categorical(
            data_filtered['raceethnicity'],
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
    heatmap = alt.Chart(data_filtered).mark_circle(opacity=0.6, size=35).encode(
        longitude='longitude:Q',
        latitude='latitude:Q',
        color=alt.Color('raceethnicity', scale=alt.Scale(scheme='category10')),
        tooltip=['latitude:Q', 'longitude:Q', 'raceethnicity', 'state']
    )
    return (us_map + heatmap).to_dict()


@callback(
    Output('race_bar', 'spec'),
    Input('year', 'value')
)
def create_race_bar(year):
    data_filtered = data
    if year != '2015 & 2016':
        data_filtered = data_filtered[data_filtered['year'] == year]
    return alt.Chart(data_filtered).mark_bar().encode(
            x = 'count()',
            y = alt.Y('raceethnicity').sort('-x'),
            color = 'gender',
            tooltip = 'count()'
        ).properties(
            title = 'Race/Ethnicity Distribution of Police Killings Victims'    
        ).interactive(           
        ).to_dict()

@callback(
    Output("race-checklist", "value"),
    Output("all-checklist", "value"),
    Input("race-checklist", "value"),
    Input("all-checklist", "value"),
)
def sync_checklists(race_selected, all_selected):
    ctx = callback_context
    options = ['Black', 'White', 'Hispanic/Latino',
               'Asian/Pacific Islander', 'Native American', 
               'Arab-American', 'Other']
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "race-checklist":
        all_selected = ["All"] if set(race_selected) == set(options) else []
    else:
        race_selected = options if all_selected else []
    return race_selected, all_selected

# @callback(
#     Output('top10_bar', 'spec'),
#     Input('year', 'value'),
#     #Input('race', 'value')
# )
# def create_top10_bar(year):
#     data_filtered = data
#     if year != 'Both':
#         data_filtered = data_filtered[data_filtered['year'] == int(year)]
#     # if race is not None:
#     #     data_filtered = data_filtered[data_filtered['raceethnicity'].isin(race)]
#     #     data_filtered['raceethnicity'] = pd.Categorical(
#     #         data_filtered['raceethnicity'],
#     #         categories=race,
#     #         ordered=True
#     #         )
#     return alt.Chart(data_filtered).transform_aggregate(
#             count='count()', 
#             groupby=['state']
#         ).transform_window(
#             rank='rank()',
#             sort=[alt.SortField('count', order='descending')]
#         ).transform_filter(
#             alt.datum.rank <= 10
#         ).mark_bar().encode(
#             x=alt.X('count:Q', title='Police Killing Count'),
#             y=alt.Y('state', sort='-x', title='States'),
#             tooltip = 'count:Q'
#         ).properties(
#             title='Top 10 States by Police Killings'
#         ).to_dict()

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)