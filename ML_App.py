import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import joblib
import plotly.graph_objs as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])


app.layout = dbc.Container([

    dbc.Row(
        dbc.Col(html.H1("Forecasting Tool",
                        className='text-center text-primary mb-4'),
                width=12)
    ),

    dbc.Row(
        dbc.Col(html.H3("Number of hospital beds required for new area in Australia",
                        className='text-center text-primary mb-4'),
                width=12)
    ),
    dbc.Row([
        dbc.Col([          
            dbc.Label("Population of New Area: ",
                   style={"textDecoration": "underline"}),

            dbc.Input(id='area_population', placeholder='100000', type='text'),
            html.Br(),
                          
        ], 
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

        dbc.Col([
            dbc.Label("Median Annual Income of New Area: ",
                   style={"textDecoration": "underline"}),

            dbc.Input(id='median_annual_income', placeholder='100000', type='text'),
            html.Br(),
                          
        ], 
           xs=12, sm=12, md=12, lg=5, xl=5
        ),
    ], no_gutters=False, justify='center'),

    dbc.Row([
        dbc.Col([
            dbc.Label("Number of Dwellings: ",
                   style={"textDecoration": "underline"}),

            dbc.Input(id='dwelling_no', placeholder='100000', type='text'),
            html.Br(),
                          
        ], 
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

        dbc.Col([
            dbc.Label("Number of people earning income: ",
                   style={"textDecoration": "underline"}),

            dbc.Input(id='No_of_people_earning_income', placeholder='100000', type='text'),
            html.Br(),
                          
        ], 
           xs=12, sm=12, md=12, lg=5, xl=5
        ),
    ], no_gutters=False, justify='center'),

    dbc.Row([
        dbc.Col([
            dbc.Label("Number of people who are tertiary_educated: ",
                   style={"textDecoration": "underline"}),

            dbc.Input(id='No_of_tertiary_educated', placeholder='100000', type='text'),
            html.Br(),
                          
        ], 
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

        dbc.Col([
            dbc.Label("The Average Monthly Mortgage Repayment: ",
                   style={"textDecoration": "underline"}),

            dbc.Input(id='Monthly_Mortgage_Repayment', placeholder='100000', type='text'),
            html.Br(),
                          
        ], 
           xs=12, sm=12, md=12, lg=5, xl=5
        ),
    ], no_gutters=False, justify='center'),  

    dbc.Row([
        dbc.Col([
            dbc.Label("Number of renters: ",
                   style={"textDecoration": "underline"}),

            dbc.Input(id='Number_of_renters', placeholder='100000', type='text'),
            html.Br(),
                          
        ], 
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

        dbc.Col([
            dbc.Label("Number of indigenous people:  ",
                   style={"textDecoration": "underline"}),

            dbc.Input(id='No_of_indigenous_ppl', placeholder='100000', type='text'),
            html.Br(),
                          
        ], 
           xs=12, sm=12, md=12, lg=5, xl=5
        ),
    ], no_gutters=False, justify='center', ),

    dbc.Row([
        dbc.Col(dbc.CardBody([html.H4("Machine Learning Prediction", className="card-title"),
                    html.P(
                    "When all the inputs are entered above "
                    "the number of hospital beds required/predicted is shown below:",
                    className="card-text center",
                    ),
                    dbc.Label(id='result', color="primary", className="font-weight-bold mb-4 display-1")]),
                xs=12, sm=12, md=12, lg=5, xl=5)
], no_gutters=False, justify='center',)
     

], fluid=True)




@app.callback(
    Output(component_id='result', component_property='children'),
    Input(component_id='area_population', component_property='value'),
    Input(component_id='median_annual_income', component_property='value'),
    Input(component_id='dwelling_no', component_property='value'),
    Input(component_id='No_of_people_earning_income', component_property='value'),
    Input(component_id='No_of_tertiary_educated', component_property='value'),
    Input(component_id='Monthly_Mortgage_Repayment', component_property='value'),
    Input(component_id='Number_of_renters', component_property='value'),
    Input(component_id='No_of_indigenous_ppl', component_property='value'))

def hosp_bed_pred(
    area_population,
    median_annual_income,
    dwelling_no,
    No_of_people_earning_income,
    No_of_tertiary_educated,
    Monthly_Mortgage_Repayment,
    Number_of_renters,
    No_of_indigenous_ppl):


    if area_population != None and \
        area_population != '' and \
        median_annual_income != None and \
        median_annual_income != '' and \
        dwelling_no != None and \
        dwelling_no != '' and \
        No_of_people_earning_income != None and \
        No_of_people_earning_income != '' and \
        No_of_tertiary_educated != None and \
        No_of_tertiary_educated != '' and \
        Monthly_Mortgage_Repayment != None and \
        Monthly_Mortgage_Repayment != '' and \
        Number_of_renters != None and \
        Number_of_renters != '' and \
        No_of_indigenous_ppl != None and \
        No_of_indigenous_ppl != '':
        try:
            hosp_beds = model.predict([[int(area_population), int(median_annual_income), int(dwelling_no), int(No_of_people_earning_income), int(No_of_tertiary_educated), int(Monthly_Mortgage_Repayment), int(Number_of_renters), int(No_of_indigenous_ppl)]])[0]
            print(hosp_beds)
            return '{:.0f}'.\
                format(hosp_beds, 0)
        except ValueError:
            print(hosp_beds)
            return 'Unable to give years of experience'


if __name__ == '__main__':
    model = joblib.load("./Model/hospital_bed_pred.pkl")
    app.run_server(debug=True)