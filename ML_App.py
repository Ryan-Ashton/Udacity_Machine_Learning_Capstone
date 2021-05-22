import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import joblib

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

            dbc.Input(id='area_population', placeholder='8237', type='text'),
            html.Br(),
                          
        ], 
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

        dbc.Col([
            dbc.Label("Median Annual Income of New Area: ",
                   style={"textDecoration": "underline"}),

            dbc.Input(id='median_annual_income', placeholder='53634', type='text'),
            html.Br(),
                          
        ], 
           xs=12, sm=12, md=12, lg=5, xl=5
        ),
    ], no_gutters=False, justify='center'),

    dbc.Row([
        dbc.Col([
            dbc.Label("Number of Dwellings: ",
                   style={"textDecoration": "underline"}),

            dbc.Input(id='dwelling_no', placeholder='3749', type='text'),
            html.Br(),
                          
        ], 
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

        dbc.Col([
            dbc.Label("Number of people who are tertiary_educated: ",
                   style={"textDecoration": "underline"}),

            dbc.Input(id='No_of_tertiary_educated', placeholder='851', type='text'),
            html.Br(),
                          
        ], 
           xs=12, sm=12, md=12, lg=5, xl=5
        ),
    ], no_gutters=False, justify='center'),

 
    dbc.Row([
        dbc.Col(dbc.CardBody([html.H4("Machine Learning Prediction", className="card-title"),
                    html.P(
                    "When all the inputs are entered above - "
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
    Input(component_id='No_of_tertiary_educated', component_property='value'))


def hosp_bed_pred(
    area_population,
    median_annual_income,
    dwelling_no,
    No_of_tertiary_educated):


    if area_population != None and \
        area_population != '' and \
        median_annual_income != None and \
        median_annual_income != '' and \
        dwelling_no != None and \
        dwelling_no != '' and \
        No_of_tertiary_educated != None and \
        No_of_tertiary_educated != '':
        try:
            hosp_beds = model.predict([[int(area_population), int(dwelling_no), int(median_annual_income),  int(No_of_tertiary_educated)]])[0]
            print(hosp_beds)
            return '{:.0f}'.\
                format(hosp_beds, 0)
        except ValueError:
            print(hosp_beds)
            return 'Unable to provide hospital bed numbers'


if __name__ == '__main__':
    model = joblib.load("./Model/hospital_bed_pred.pkl")
    app.run_server(debug=True)