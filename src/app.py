import altair as alt
from dash import Dash, html, dcc, Input, Output, callback_context, callback, no_update
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
from dash.exceptions import PreventUpdate

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Add this line for deployment compatibility
server = app.server

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
            html.H3('Global Controls'),
            html.H5('Year'),
            dcc.RadioItems(
                id='year',
                options=[2015, 2016, '2015 & 2016'], 
                value='2015 & 2016'
                ),
            html.Br(),

            html.H5('Race/Ethnicity'),
            dcc.Checklist(["All"], ["All"], id="all-checklist-1", inline=True),
            dcc.Checklist(
                id='race-checklist', 
                options=['White', 'Black', 'Hispanic/Latino', 
                         'Asian/Pacific Islander', 'Native American', 
                         'Arab-American', 'Other'],
                ), 
            
            html.Br(),
            html.H5('Age Group'),
            dcc.Checklist(["All"], ["All"], id="all-checklist-2", inline=True),
            dcc.Checklist(
                id='age-checklist', 
                options=['Under 19', '20-39', '40-59', 'Above 60', 'Unknown'],
                ),

            html.Br(),
            html.H5('Is the victim armed?'),
            dcc.Checklist(["All"], ["All"], id="all-checklist-3", inline=True),
            dcc.Checklist(
                id='armed-checklist', 
                options=['No', 'Firearm', 'Non-lethal firearm', 'Knife', 'Vehicle', 'Disputed', 'Other']
                ),
        ]),

        dbc.Col([
            dbc.Tabs([
                dbc.Tab([
                    dvc.Vega(id='map', spec={}),
                ], label='US Map Distribution'),
                dbc.Tab([
                    dvc.Vega(id='race_bar', spec={}),
                ], label='Race/Ethnicity Summary Distribution'),
            ]),
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H5('Type the number of top states'),
                        dcc.Input(id='top_state', placeholder='Integer between 0 and 51', debounce=True, min=0, max=51),
                        html.P(id='err', style={'color': 'red'}),
                        html.P(id='output_area')
                    ], style={'textAlign': 'center'}),
                    dbc.Row([
                        dbc.Col([dvc.Vega(id='top10_bar', spec={})]),
                        dbc.Col([dvc.Vega(id='time_series', spec={})]),
                    ]),
                ]),
            ]),
        ], md=10),
    ])
])

# Server side callbacks/reactivity
@callback(
    Output('map', 'spec'),
    Output('race_bar', 'spec'),
    Output('top10_bar', 'spec'),
    Output('time_series', 'spec'),
    Input('year', 'value'),
    Input('race-checklist', 'value'),
    Input('age-checklist', 'value'), 
    Input('armed-checklist', 'value'), 
    Input('top_state', 'value'), 
)
def create_chart(year, race, age, armed, top_state):
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
    if age is not None:
        data_filtered = data_filtered[data_filtered['age_group'].isin(age)]
        data_filtered['age_group'] = pd.Categorical(
            data_filtered['age_group'],
            categories=age,
            ordered=True
            )
    if armed is not None:
        data_filtered = data_filtered[data_filtered['armed'].isin(armed)]
        data_filtered['armed'] = pd.Categorical(
            data_filtered['armed'],
            categories=armed,
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
        tooltip=['latitude:Q', 'longitude:Q', 'raceethnicity', 'state', 'armed']
    )
    map = (us_map + heatmap).to_dict()
    
    bar = alt.Chart(data_filtered).mark_bar().encode(
            x = 'count()',
            y = alt.Y('raceethnicity').sort('-x'),
            color = 'gender',
            tooltip = 'count()'
        ).properties(
            title = 'Race/Ethnicity Distribution of Police Killings Victims', 
            height=300, 
            width=500
        ).to_dict()
    
    if top_state is None:
        top_state = '0'
    elif (not top_state.isdigit()) or (int(top_state) > 51):
        return map, bar, no_update, no_update

    top10 = alt.Chart(data_filtered).transform_aggregate(
            count='count()', 
            groupby=['state']
        ).transform_window(
            rank='rank()',
            sort=[alt.SortField('count', order='descending')]
        ).transform_filter(
            alt.datum.rank <= int(top_state)
        ).mark_bar().encode(
            x=alt.X('count:Q', title='Police Killing Count'),
            y=alt.Y('state', sort='-x', title='States'),
            tooltip = 'count:Q'
        ).properties(
            title=f'Top {top_state} States by Police Killings',
            width=250
        ).to_dict()
    
    states = data_filtered['state'].value_counts()[:int(top_state)].index.to_list()
    data_filtered = data_filtered[data_filtered['state'].isin(states)]
    time = alt.Chart(data_filtered).mark_line().encode(
            x=alt.X('yearmonth(date):O', title='Month of Year'),
            y=alt.Y('count()', title='Number of Killings'),
            color='state',
            tooltip=['yearmonth(date):O', 'count()', 'state']
        ).properties(
            title = 'Police Killings Victims by Months', 
            height=400, 
            width=440
        ).interactive().to_dict()
    return map, bar, top10, time

@callback(
    Output('output_area', 'children'),
    Output('err', 'children'),
    Input('top_state', 'value'))
def update_output(input_value):
    if input_value is None:
        raise PreventUpdate
    if not input_value.isdigit():
        return no_update, f'{input_value} is not an integer between 0 and 51. No updates are made until correction.'
    elif (int(input_value) > 51):
        return no_update, f'{input_value} is not an integer between 0 and 51. No updates are made until correction.'
    return f'Showing {input_value} states for these two plots.', ''

@callback(
    Output("race-checklist", "value"),
    Output("all-checklist-1", "value"),
    Input("race-checklist", "value"),
    Input("all-checklist-1", "value")
)
def sync_race_checklists(race_selected, all_selected):
    ctx = callback_context
    race_options = ['White', 'Black', 'Hispanic/Latino',
               'Asian/Pacific Islander', 'Native American', 
               'Arab-American', 'Other']
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "race-checklist":
        all_selected = ["All"] if set(race_selected) == set(race_options) else []
    else:
        race_selected = race_options if all_selected else []
    return race_selected, all_selected

@callback(
    Output("age-checklist", "value"),
    Output("all-checklist-2", "value"),
    Input("age-checklist", "value"),
    Input("all-checklist-2", "value")
)
def sync_age_checklists(age_selected, all_selected):
    ctx = callback_context
    age_options = ['20-39', '40-59', 'Under 19', 'Above 60', 'Unknown']
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "age-checklist":
        all_selected = ["All"] if set(age_selected) == set(age_options) else []
    else:
        age_selected = age_options if all_selected else []
    return age_selected, all_selected

@callback(
    Output("armed-checklist", "value"),
    Output("all-checklist-3", "value"),
    Input("armed-checklist", "value"),
    Input("all-checklist-3", "value")
)
def sync_armed_checklists(armed_selected, all_selected):
    ctx = callback_context
    armed_options = ['No', 'Firearm', 'Non-lethal firearm', 'Knife', 'Vehicle', 'Disputed', 'Other']
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "armed-checklist":
        all_selected = ["All"] if set(armed_selected) == set(armed_options) else []
    else:
        armed_selected = armed_options if all_selected else []
    return armed_selected, all_selected

# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=False)