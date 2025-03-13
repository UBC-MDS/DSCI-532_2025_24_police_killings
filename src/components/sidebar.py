import dash_bootstrap_components as dbc
from dash import html, dcc
import callbacks

def year_card():
    '''Create a card to contain the year filters'''
    year_options = [2015, 2016]
    card = dbc.Card([
        dbc.CardHeader(
            html.H5('Year'),
            className='custom-filter-title'
            ),
        dbc.CardBody(
            dbc.Col(
                dcc.Checklist(
                    id='year',
                    options=[{
                        'label': html.Span(year, style={'margin-left': '5px', 'margin-right': '10px'}), 
                        'value': year
                        } for year in year_options], 
                    inline=True
                ), className="text-center"
            )
        )
    ])
    return card

def race_dropdown():
    '''Create a card to contain the race filters'''
    race_options = ['White', 'Black', 'Hispanic/Latino', 
                    'Asian/Pacific Islander', 'Native American', 
                    'Arab-American', 'Other']
    drop = dcc.Dropdown(
        id='race-dropdown',
        options=race_options,
        multi=True,
    )
    drop_menu = dbc.Card([
        dbc.CardHeader(
            html.H5('Race/Ethnicity'),
            className='custom-filter-title'
        ),
        dbc.CardBody([
            drop
        ])
    ])
    return drop_menu

def age_dropdown():
    '''Create a card to contain the age filters'''
    age_options = ['Under 19', '20-39', '40-59', 'Above 60', 'Unknown']

    drop = dcc.Dropdown(
        id='age-dropdown',
        options=age_options,
        multi=True,
    )
    drop_menu = dbc.Card([
        dbc.CardHeader(
            html.H5('Age Group'),
            className='custom-filter-title'
            ),
        dbc.CardBody([
            drop
        ])
    ])
    return drop_menu

def armed_dropdown():
    '''Create a card to contain the armed filters'''
    armed_options = ['Unarmed', 'Firearm', 'Non-lethal firearm', 'Knife', 'Vehicle', 'Disputed', 'Other']

    drop = dcc.Dropdown(
        id='armed-dropdown',
        options=armed_options,
        multi=True,
    )
    drop_menu = dbc.Card([
        dbc.CardHeader(
            html.H5('Armed Status of Deceased'),
            className='custom-filter-armed'
            ),
        dbc.CardBody([
            drop
        ])
    ])
    return drop_menu

sidebar = dbc.Col([
    html.H3('Global Controls', className="text-center"),
    year_card(),
    html.Br(),
    race_dropdown(),
    html.Br(),
    age_dropdown(),
    html.Br(),
    armed_dropdown()
    ], 
    md=2, className="custom-sidebar")