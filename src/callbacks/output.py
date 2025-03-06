from dash import Input, Output, callback, no_update

@callback(
    Output('output_area', 'children'),
    Input('top_state', 'value'))
def update_output(input_value):
    return f'Showing top {input_value} states. Click on the bars in the barplot to view the police killings over time in the corresponding state.'
