from dash import Input, Output, callback, callback_context, no_update
from dash.exceptions import PreventUpdate  # ✅ Correct way to import PreventUpdate

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
    return f'Showing top {input_value} states. Click on the bars in the barplot to view the police killings over time for the corresponding state.', ''

@callback(
    Output("race-checklist", "value"),
    Output("all-checklist-1", "value"),
    Input("race-checklist", "value"),
    Input("all-checklist-1", "value")
)
def sync_race_checklists(race_selected, all_selected):
    ctx = callback_context
    race_options = ['White', 'Black', 'Hispanic/Latino',
               'Asian/Pacific Islander', 'Native American', 
               'Arab-American', 'Other']
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "race-checklist":
        all_selected = ["All"] if set(race_selected) == set(race_options) else []
    else:
        race_selected = race_options if all_selected else []
    return race_selected, all_selected

@callback(
    Output("age-checklist", "value"),
    Output("all-checklist-2", "value"),
    Input("age-checklist", "value"),
    Input("all-checklist-2", "value")
)
def sync_age_checklists(age_selected, all_selected):
    ctx = callback_context
    age_options = ['20-39', '40-59', 'Under 19', 'Above 60', 'Unknown']
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "age-checklist":
        all_selected = ["All"] if set(age_selected) == set(age_options) else []
    else:
        age_selected = age_options if all_selected else []
    return age_selected, all_selected

@callback(
    Output("armed-checklist", "value"),
    Output("all-checklist-3", "value"),
    Input("armed-checklist", "value"),
    Input("all-checklist-3", "value")
)
def sync_armed_checklists(armed_selected, all_selected):
    ctx = callback_context
    armed_options = ['Unarmed', 'Firearm', 'Non-lethal firearm', 'Knife', 'Vehicle', 'Disputed', 'Other']
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "armed-checklist":
        all_selected = ["All"] if set(armed_selected) == set(armed_options) else []
    else:
        armed_selected = armed_options if all_selected else []
    return armed_selected, all_selected
