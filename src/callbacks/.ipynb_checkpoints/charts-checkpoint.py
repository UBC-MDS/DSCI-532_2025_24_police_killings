from dash import Input, Output, callback, no_update
import altair as alt
from utils.data_loader import data
import pandas as pd  # ✅ Add this import

@callback(
    Output('us_map_chart', 'spec'),
    Output('race_bar', 'spec'),
    Output('top10_time', 'spec'),
    Input('year', 'value'),
    Input('race-checklist', 'value'),
    Input('age-checklist', 'value'), 
    Input('armed-checklist', 'value'), 
    Input('top_state', 'value')
)
def create_chart(year, race, age, armed, top_state):
    data_filtered = data.copy()

    # Apply Year Filter
    if year != '2015 & 2016':
        data_filtered = data_filtered[data_filtered['year'] == year]

    # Apply Race Filter
    if race is not None:
        data_filtered = data_filtered[data_filtered['raceethnicity'].isin(race)]
        data_filtered['raceethnicity'] = pd.Categorical(
            data_filtered['raceethnicity'], 
            categories=race, 
            ordered=True)

    # Apply Age Filter
    if age is not None:
        data_filtered = data_filtered[data_filtered['age_group'].isin(age)]
        data_filtered['age_group'] = pd.Categorical(
            data_filtered['age_group'], 
            categories=age, 
            ordered=True)

    # Apply Armed Status Filter
    if armed is not None:
        data_filtered = data_filtered[data_filtered['armed'].isin(armed)]
        data_filtered['armed'] = pd.Categorical(
            data_filtered['armed'], 
            categories=armed, 
            ordered=True)

    # Load US Map Data
    us_map_url = "https://vega.github.io/vega-datasets/data/us-10m.json"
    us_map = alt.Chart(alt.topo_feature(us_map_url, 'states')).mark_geoshape(
        fill='lightgray', stroke='white'
    ).project(
        type='albersUsa'
    ).properties(
        title='Police Killings Across the United States', 
        width=950, 
        height=500)

    heatmap = alt.Chart(data_filtered).mark_circle(opacity=0.5, size=45).encode(
        longitude='longitude:Q',
        latitude='latitude:Q',
        color=alt.Color('raceethnicity', scale=alt.Scale(scheme='category10')),
        tooltip=['latitude:Q', 'longitude:Q', 'raceethnicity', 'state', 'armed']
    )

    map = (us_map + heatmap).to_dict()

    # Bar Chart for Race/Ethnicity Distribution
    bar = alt.Chart(data_filtered).mark_bar().encode(
        x='count()',
        y=alt.Y('raceethnicity').sort('-x'),
        color='gender',
        tooltip='count()'
    ).properties(
        title='Race/Ethnicity Distribution of Police Killings Victims', 
        height=300, 
        width=500).to_dict()

    # Handle Top State Input
    if top_state is None:
        top_state = '0'
    elif (not top_state.isdigit()) or (int(top_state) > 51):
        return map, bar, no_update

    states = data_filtered['state'].value_counts()[:int(top_state)].index.to_list()
    data_filtered = data_filtered[data_filtered['state'].isin(states)]

    # Top 10 States Bar Chart
    select_state = alt.selection_point(
        fields=['state'])
    top10_chart = alt.Chart(data_filtered).mark_bar().encode(
        x=alt.X('count()', title='Police Killing Count'),
        y=alt.Y('state', sort='-x', title='States'),
        tooltip='count()',
        opacity=alt.condition(select_state, alt.value(1), alt.value(0.2))
    ).properties(
        title=f'Top {top_state} States by Police Killings', 
        width=300).add_params(select_state)

    # Time Series Chart
    time_chart = alt.Chart(data_filtered).mark_line().encode(
        x=alt.X('yearmonth(date):O', title='Month of Year'),
        y=alt.Y('count()', title='Number of Killings'),
        color='state',
        tooltip=['yearmonth(date):O', 'count()', 'state'],
        opacity=alt.condition(select_state, alt.value(0.8), alt.value(0.1))
    ).properties(
        title='Police Killings Victims by Months', 
        height=500, 
        width=500)

    top10_time_chart = (top10_chart | time_chart).to_dict()

    return map, bar, top10_time_chart