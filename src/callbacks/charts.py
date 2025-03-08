from dash import Input, Output, callback
import altair as alt
import pandas as pd
from data.police_data import police_data

data = police_data

def filter_data(data, year, race, age, armed):
    """Filter the data based on global selections."""
    df = data.copy()
    if year:
        df = df[df['year'].isin(year)]
    if race:
        df = df[df['raceethnicity'].isin(race)]
        df['raceethnicity'] = pd.Categorical(
            df['raceethnicity'],
            categories=race,
            ordered=True
            )
    if age:
        df = df[df['age_group'].isin(age)]
        df['age_group'] = pd.Categorical(
            df['age_group'],
            categories=age,
            ordered=True
            )
    if armed:
        df = df[df['armed'].isin(armed)]
        df['armed'] = pd.Categorical(
            df['armed'],
            categories=armed,
            ordered=True
            )
    return df

def create_map(data, var):
    """Create the US Map with scatter points."""
    if var == 'raceethnicity':
        label = 'Race/Ethnicity'
    elif var == 'armed':
        label = 'Armed Status'
    else:
        label = 'Age Group'

    us_map_url = "https://vega.github.io/vega-datasets/data/us-10m.json"
    us_map = alt.Chart(alt.topo_feature(us_map_url, 'states')).mark_geoshape(
        fill='lightgray', stroke='white'
    ).project(
        type='albersUsa'
    ).properties(
        width=850,
        height=400
    )
    heatmap = alt.Chart(data).mark_circle(opacity=0.5, size=45).encode(
        longitude='longitude:Q',
        latitude='latitude:Q',
        color=alt.Color(var, title=label, scale=alt.Scale(scheme='category10')),
        tooltip=['name', 'state', 'raceethnicity', 'age', 'armed']
    )
    return (us_map + heatmap).configure_legend(
        labelFontSize=15,
        titleFontSize=17
    ).to_dict()


def create_bar(data, var):
    """Create the race/ethnicity barplot."""
    if var == 'raceethnicity':
        label = 'Race/Ethnicity'
    elif var == 'armed':
        label = 'Armed Status'
    else:
        label = 'Age Group'
        data['age_group'] = pd.Categorical(
            data['age_group'],
            categories=['Under 19', '20-39', '40-59', 'Above 60', 'Unknown'],
            ordered=True
        )
        bar = alt.Chart(data).mark_bar().encode(
                x = 'count()',
                y = alt.Y(var,  title=label),
                color = alt.Color('gender', title='Gender'),
                tooltip = 'count()'
            ).properties(
                height=350, 
                width=450
            ).configure_axis(
                labelFontSize=14,  
                titleFontSize=16
            ).configure_legend(
                labelFontSize=14, 
                titleFontSize=16
            ).to_dict()
        return bar

    bar = alt.Chart(data).mark_bar().encode(
            x = 'count()',
            y = alt.Y(var,  title=label).sort('-x'),
            color = alt.Color('gender', title='Gender'),
            tooltip = 'count()'
        ).properties(
            height=350, 
            width=450
        ).configure_axis(
            labelFontSize=14,  
            titleFontSize=16
        ).configure_legend(
            labelFontSize=14, 
            titleFontSize=16
        ).to_dict()
    return bar

def filter_states(data, top_state):
    """Filter the data based on the number of top states input."""
    states = data['state'].value_counts()[:top_state].index.to_list()
    df = data[data['state'].isin(states)]
    return df

def create_state_time(data, top_state):
    """Create the combined plots of top states barplot and time-series line plot"""
    select_state = alt.selection_point(
        fields=['state'])
    top10 = alt.Chart(data).mark_bar().encode(
            x=alt.X('count()', title='Police Killing Count'),
            y=alt.Y('state', sort='-x', title='States'),
            tooltip = 'count()',
            opacity=alt.condition(select_state, alt.value(1), alt.value(0.2))
        ).add_params(
            select_state
        ).properties(
            title=f'Top {top_state} States by Police Killings',
            height=400,
            width=230
        )

    color_list = [
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
        "#aec7e8", "#ffbb78", "#98df8a", "#ff9896", "#c5b0d5", "#c49c94", "#f7b6d2", "#c7c7c7", "#dbdb8d", "#9edae5",
        "#393b79", "#637939", "#8c6d31", "#843c39", "#7b4173"
    ]
    time = alt.Chart(data).mark_line().encode(
            x=alt.X('yearmonth(date):O', title='Month of Year'),
            y=alt.Y('count()', title='Number of Killings'),
            color=alt.Color(
                'state', 
                title='State', 
                scale=alt.Scale(
                    domain=data['state'].unique(),
                    range=color_list[:len(data['state'].unique())]
                )
            ),
            tooltip=['yearmonth(date):O', 'count()', 'state'],
            opacity=alt.condition(
                select_state, alt.value(0.8), alt.value(0.1)
            )
        ).properties(
            title = 'Police Killings Victims by Months', 
            height=400, 
            width=500
        )
    top10_time = (top10 | time).configure_axis(
            labelFontSize=14,  
            titleFontSize=16   
        ).configure_title(
            fontSize=18  
        ).configure_legend(
            labelFontSize=14, 
            titleFontSize=16
        ).to_dict()
    return top10_time

# Server side callbacks/reactivity
@callback(
    Output('map', 'spec'),
    Output('race_bar', 'spec'),
    Output('top10_time', 'spec'),
    Input('year', 'value'),
    Input('race-dropdown', 'value'),
    Input('age-dropdown', 'value'), 
    Input('armed-dropdown', 'value'),
    Input('map_dropdown', 'value'), 
    Input('bar_dropdown', 'value'), 
    Input('top_state', 'value'), 
)
def create_chart(year, race, age, armed, map_dropdown, bar_dropdown, top_state):
    data_filtered = filter_data(data, year, race, age, armed)
    
    map = create_map(data_filtered, map_dropdown)
    bar = create_bar(data_filtered, bar_dropdown)

    data_filtered = filter_states(data_filtered, top_state)
    top10_time = create_state_time(data_filtered, top_state)

    return map, bar, top10_time
