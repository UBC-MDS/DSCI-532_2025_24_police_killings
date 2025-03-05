from dash import html, dcc

input_state = html.Div([
        html.H5('Enter the number of top states below:'),
        dcc.Input(id='top_state', placeholder='Integer between 0 and 51', debounce=False, min=0, max=51),
        html.P(id='err', style={'color': 'red'}),
        html.P(id='output_area')
    ], style={
        'background-color': '#E4AA90',
        'padding': 9,
        }
    )