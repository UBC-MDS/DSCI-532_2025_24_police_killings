from dash import Input, Output, callback, no_update
from dash.exceptions import PreventUpdate

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
    return f'Showing top {input_value} states. Click on the bars in the barplot to view the police killings over time in the corresponding state.', ''
