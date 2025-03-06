from dash import Input, Output, State, callback_context, callback, no_update

@callback(
    Output("race-dropdown", "value"),
    Input("select-all-race", "n_clicks"),
    State("race-dropdown", "value"),
    prevent_initial_call=True
)
def select_all_race(n_clicks, selected_values):
    race_options = ['White', 'Black', 'Hispanic/Latino',
                    'Asian/Pacific Islander', 'Native American', 
                    'Arab-American', 'Other']
    ctx = callback_context
    if ctx.triggered_id == "select-all-race":
        return [opt for opt in race_options]
    return no_update

@callback(
    Output("age-dropdown", "value"),
    Input("select-all-age", "n_clicks"),
    State("age-dropdown", "value"),
    prevent_initial_call=True
)
def select_all_age(n_clicks, selected_values):
    age_options = ['Under 19', '20-39', '40-59', 'Above 60', 'Unknown']
    ctx = callback_context
    if ctx.triggered_id == "select-all-age":
        return [opt for opt in age_options]
    return no_update

@callback(
    Output("armed-dropdown", "value"),
    Input("select-all-armed", "n_clicks"),
    State("armed-dropdown", "value"),
    prevent_initial_call=True
)
def select_all_armed(n_clicks, selected_values):
    armed_options = ['Unarmed', 'Firearm', 'Non-lethal firearm', 'Knife', 'Vehicle', 'Disputed', 'Other']
    ctx = callback_context
    if ctx.triggered_id == "select-all-armed":
        return [opt for opt in armed_options]
    return no_update