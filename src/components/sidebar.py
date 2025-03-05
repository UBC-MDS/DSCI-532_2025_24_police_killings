import dash_bootstrap_components as dbc
from dash import html, dcc

year_options = [2015, 2016, '2015 & 2016']
race_options = ['White', 'Black', 'Hispanic/Latino', 
                'Asian/Pacific Islander', 'Native American', 
                'Arab-American', 'Other']
age_options = ['Under 19', '20-39', '40-59', 'Above 60', 'Unknown']
armed_options = ['Unarmed', 'Firearm', 'Non-lethal firearm', 'Knife', 'Vehicle', 'Disputed', 'Other']

sidebar = dbc.Col([
    html.H3('Global Controls'),
    html.H5('Year'),
    dcc.RadioItems(
        id='year',
        options=[2015, 2016, '2015 & 2016'], 
        value='2015 & 2016'
        ),
    html.Br(),

    html.H5('Race/Ethnicity'),
    dcc.Checklist(options=[{'label': html.Span('All', style={'margin-left': '10px'}), 'value': 'All'}], 
                  value=["All"], id="all-checklist-1", inline=True),
    dcc.Checklist(
        id='race-checklist', 
        options=[{'label': html.Span(race, style={'margin-left': '10px'}), 'value': race} for race in race_options]
        ), 
    
    html.Br(),
    html.H5('Age Group'),
    dcc.Checklist(options=[{'label': html.Span('All', style={'margin-left': '10px'}), 'value': 'All'}], 
                  value=["All"], id="all-checklist-2", inline=True),
    dcc.Checklist(
        id='age-checklist', 
        options=[{'label': html.Span(age, style={'margin-left': '10px'}), 'value': age} for age in age_options],
        ),

    html.Br(),
    html.H5('Was the Victim Armed?'),
    dcc.Checklist(options=[{'label': html.Span('All', style={'margin-left': '10px'}), 'value': 'All'}], 
                  value=["All"], id="all-checklist-3", inline=True),
    dcc.Checklist(
        id='armed-checklist', 
        options=[{'label': html.Span(armed, style={'margin-left': '10px'}), 'value': armed} for armed in armed_options]
        ),
    ],
    md=2, className="custom-sidebar")