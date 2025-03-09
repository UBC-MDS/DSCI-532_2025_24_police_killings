from dash import Input, Output, callback

@callback(
    Output('output_area', 'children'),
    Input('top_state', 'value'))
def update_output(input_value):
    return f'Showing top {input_value} states. Click on each bar in the barplot to view the police killings over time in the corresponding state.'
