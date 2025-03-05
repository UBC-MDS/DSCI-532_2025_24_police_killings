import dash_bootstrap_components as dbc
from dash import html, dcc

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
    html.H5('Was the Victim Armed?'),
    dcc.Checklist(["All"], ["All"], id="all-checklist-3", inline=True),
    dcc.Checklist(
        id='armed-checklist', 
        options=['Unarmed', 'Firearm', 'Non-lethal firearm', 'Knife', 'Vehicle', 'Disputed', 'Other']
        ),
    ],
    md=2, className="custom-sidebar")