######-----Import Dash-----#####
import dash
from dash import dcc
from dash import html, callback, dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

from datetime import date
from dateutil.relativedelta import relativedelta

import plotly.graph_objects as go

dash.register_page(__name__, name='Barge') # '/' is home page

##-----page 4

## -----LAYOUT-----
layout = html.Div([
                html.Br(),
                        html.P(children=[html.Strong('Barge')], 
                               style={'textAlign': 'center', 'fontSize': 27, 'background-color':'white','color':'#2a3f5f','font-family':'Verdana'}),
                ## --ROW1--
                dbc.Row([
                    dbc.Col([
                        html.Br(),
                        html.P(children=[html.Strong('Annual Survey')], 
                               style={'textAlign': 'center', 'fontSize': 22, 'background-color':'white','color':'#2a3f5f','font-family':'Verdana'}),

                        dbc.Row([###### Annual Summary
                            dbc.Col([
                                dbc.CardGroup([
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.P(children=[html.Strong('Summary')],
                                                        style={'textAlign': 'center', 
                                                            'fontSize': 16, 
                                                            'background-color':'white',
                                                            'color':'#2a3f5f',
                                                            'font-family':'Verdana'}),
                                            ]
                                        ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px"}
                                    ),
                                    dbc.Card(
                                        html.Div(className='bi bi-info-square', style={
                                                                                "color": "white",
                                                                                "textAlign": "center",
                                                                                "fontSize": 30,
                                                                                "margin": "auto",
                                                                            }),
                                        className='bg-secondary',
                                        color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                    ),
                                ],),
                            ], xs=5),
                            ###### Annual Alerts
                            dbc.Col([
                                dbc.CardGroup([
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.P(children=[html.Strong('Alerts')],
                                                        style={'textAlign': 'Center', 
                                                            'fontSize': 16, 
                                                            'background-color':'white',
                                                            'color':'#2a3f5f',
                                                            'font-family':'Verdana'}),
                                            ]
                                        ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px"}
                                    ),
                                    dbc.Card(
                                        html.Div(className='bi bi-exclamation-square', style={
                                                                                "color": "white",
                                                                                "textAlign": "center",
                                                                                "fontSize": 30,
                                                                                "margin": "auto",
                                                                            }),
                                        className='bg-warning',
                                        color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                    ),
                                ],),
                            ], xs=7),
                        ], className="g-0 d-flex align-items-center"),

                        dbc.Row([
                            ###### Annual Bar Plot
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(dcc.Graph(id='annual_ba_bar'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### Annual Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_annual_ba_alerts",
                                                                               columns=[{'name':'Barge','id': 'Barge'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'Barge'},
                                                                                                        'width': '30%'},
                                                                                                        {'if': {'column_id': 'Remaining Days'},
                                                                                                        'width': '70%'},
                                                                                                        {'textAlign': 'center'}
                                                                                                    ],
                                                                               style_cell={'font-family':'Verdana',
                                                                                           'fontSize': 13,
                                                                                           'color':'#2a3f5f',},
                                                                               css=[{
                                                                                   'selector': '.dash-table-tooltip',
                                                                                   'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                               tooltip_delay=0,
                                                                               tooltip_duration=None
                                                                               )))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=7),
                        ], className="g-0 d-flex align-items-center")
                    ], xs=4),

                    dbc.Col([
                        html.Br(),
                        html.P(children=[html.Strong('Special Survey')], 
                               style={'textAlign': 'center', 'fontSize': 22, 'background-color':'white','color':'#2a3f5f','font-family':'Verdana'}),

                        dbc.Row([###### Special Summary
                            dbc.Col([
                                dbc.CardGroup([
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.P(children=[html.Strong('Summary')],
                                                        style={'textAlign': 'center', 
                                                            'fontSize': 16, 
                                                            'background-color':'white',
                                                            'color':'#2a3f5f',
                                                            'font-family':'Verdana'}),
                                            ]
                                        ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px"}
                                    ),
                                    dbc.Card(
                                        html.Div(className='bi bi-info-square', style={
                                                                                "color": "white",
                                                                                "textAlign": "center",
                                                                                "fontSize": 30,
                                                                                "margin": "auto",
                                                                            }),
                                        className='bg-secondary',
                                        color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                    ),
                                ],),
                            ], xs=5),
                            ###### Special Alerts
                            dbc.Col([
                                dbc.CardGroup([
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.P(children=[html.Strong('Alerts')],
                                                        style={'textAlign': 'Center', 
                                                            'fontSize': 16, 
                                                            'background-color':'white',
                                                            'color':'#2a3f5f',
                                                            'font-family':'Verdana'}),
                                            ]
                                        ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px"}
                                    ),
                                    dbc.Card(
                                        html.Div(className='bi bi-exclamation-square', style={
                                                                                "color": "white",
                                                                                "textAlign": "center",
                                                                                "fontSize": 30,
                                                                                "margin": "auto",
                                                                            }),
                                        className='bg-warning',
                                        color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                    ),
                                ],),
                            ], xs=7),
                        ], className="g-0 d-flex align-items-center"),

                        dbc.Row([
                            ###### Special Bar Plot
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(dcc.Graph(id='special_ba_bar'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### Special Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_special_ba_alerts",
                                                                               columns=[{'name':'Barge','id': 'Barge'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'Barge'},
                                                                                                        'width': '30%'},
                                                                                                        {'if': {'column_id': 'Remaining Days'},
                                                                                                        'width': '70%'},
                                                                                                        {'textAlign': 'center'}
                                                                                                    ],
                                                                               style_cell={'font-family':'Verdana',
                                                                                           'fontSize': 13,
                                                                                           'color':'#2a3f5f',},
                                                                               css=[{
                                                                                   'selector': '.dash-table-tooltip',
                                                                                   'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                               tooltip_delay=0,
                                                                               tooltip_duration=None
                                                                               )))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=7),
                        ], className="g-0 d-flex align-items-center")
                    ], xs=4),                    

                    dbc.Col([
                        html.Br(),
                        html.P(children=[html.Strong('Intermediate Survey')], 
                               style={'textAlign': 'center', 'fontSize': 22, 'background-color':'white','color':'#2a3f5f','font-family':'Verdana'}),

                        dbc.Row([###### Intermediate Summary
                            dbc.Col([
                                dbc.CardGroup([
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.P(children=[html.Strong('Summary')],
                                                        style={'textAlign': 'center', 
                                                            'fontSize': 16, 
                                                            'background-color':'white',
                                                            'color':'#2a3f5f',
                                                            'font-family':'Verdana'}),
                                            ]
                                        ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px"}
                                    ),
                                    dbc.Card(
                                        html.Div(className='bi bi-info-square', style={
                                                                                "color": "white",
                                                                                "textAlign": "center",
                                                                                "fontSize": 30,
                                                                                "margin": "auto",
                                                                            }),
                                        className='bg-secondary',
                                        color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                    ),
                                ],),
                            ], xs=5),
                            ###### Intermediate Alerts
                            dbc.Col([
                                dbc.CardGroup([
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.P(children=[html.Strong('Alerts')],
                                                        style={'textAlign': 'Center', 
                                                            'fontSize': 16, 
                                                            'background-color':'white',
                                                            'color':'#2a3f5f',
                                                            'font-family':'Verdana'}),
                                            ]
                                        ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px"}
                                    ),
                                    dbc.Card(
                                        html.Div(className='bi bi-exclamation-square', style={
                                                                                "color": "white",
                                                                                "textAlign": "center",
                                                                                "fontSize": 30,
                                                                                "margin": "auto",
                                                                            }),
                                        className='bg-warning',
                                        color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                    ),
                                ],),
                            ], xs=7),
                        ], className="g-0 d-flex align-items-center"),

                        dbc.Row([
                            ###### Intermediate Bar Plot
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(dcc.Graph(id='intermediate_ba_bar'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### Intermediate Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_intermediate_ba_alerts",
                                                                               columns=[{'name':'Barge','id': 'Barge'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'Barge'},
                                                                                                        'width': '30%'},
                                                                                                        {'if': {'column_id': 'Remaining Days'},
                                                                                                        'width': '70%'},
                                                                                                        {'textAlign': 'center'}
                                                                                                    ],
                                                                               style_cell={'font-family':'Verdana',
                                                                                           'fontSize': 13,
                                                                                           'color':'#2a3f5f',},
                                                                               css=[{
                                                                                   'selector': '.dash-table-tooltip',
                                                                                   'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                               tooltip_delay=0,
                                                                               tooltip_duration=None
                                                                               )))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=7),
                        ], className="g-0 d-flex align-items-center")
                    ], xs=4),
                ]),

                ## --ROW2--
                dbc.Row([
                    dbc.Col([
                        html.Br(),
                        html.P(children=[html.Strong('Docking Survey')], 
                               style={'textAlign': 'center', 'fontSize': 22, 'background-color':'white','color':'#2a3f5f','font-family':'Verdana'}),

                        dbc.Row([###### Docking Summary
                            dbc.Col([
                                dbc.CardGroup([
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.P(children=[html.Strong('Summary')],
                                                        style={'textAlign': 'center', 
                                                            'fontSize': 16, 
                                                            'background-color':'white',
                                                            'color':'#2a3f5f',
                                                            'font-family':'Verdana'}),
                                            ]
                                        ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px"}
                                    ),
                                    dbc.Card(
                                        html.Div(className='bi bi-info-square', style={
                                                                                "color": "white",
                                                                                "textAlign": "center",
                                                                                "fontSize": 30,
                                                                                "margin": "auto",
                                                                            }),
                                        className='bg-secondary',
                                        color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                    ),
                                ],),
                            ], xs=5),
                            ###### Docking Alerts
                            dbc.Col([
                                dbc.CardGroup([
                                    dbc.Card(
                                        dbc.CardBody(
                                            [
                                                html.P(children=[html.Strong('Alerts')],
                                                        style={'textAlign': 'Center', 
                                                            'fontSize': 16, 
                                                            'background-color':'white',
                                                            'color':'#2a3f5f',
                                                            'font-family':'Verdana'}),
                                            ]
                                        ), color="light", outline=True, style={"height": 55, "margin-bottom": "5px"}
                                    ),
                                    dbc.Card(
                                        html.Div(className='bi bi-exclamation-square', style={
                                                                                "color": "white",
                                                                                "textAlign": "center",
                                                                                "fontSize": 30,
                                                                                "margin": "auto",
                                                                            }),
                                        className='bg-warning',
                                        color="light", outline=True, style={"height": 55, "margin-bottom": "5px", "maxWidth": 75}
                                    ),
                                ],),
                            ], xs=7),
                        ], className="g-0 d-flex align-items-center"),

                        dbc.Row([
                            ###### Docking Bar Plot
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(dcc.Graph(id='docking_ba_bar'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### docking Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_docking_ba_alerts",
                                                                               columns=[{'name':'Barge','id': 'Barge'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'Barge'},
                                                                                                        'width': '30%'},
                                                                                                        {'if': {'column_id': 'Remaining Days'},
                                                                                                        'width': '70%'},
                                                                                                        {'textAlign': 'center'}
                                                                                                    ],
                                                                               style_cell={'font-family':'Verdana',
                                                                                           'fontSize': 13,
                                                                                           'color':'#2a3f5f',},
                                                                               css=[{
                                                                                   'selector': '.dash-table-tooltip',
                                                                                   'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                                                                               tooltip_delay=0,
                                                                               tooltip_duration=None
                                                                               )))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=7),
                        ], className="g-0 d-flex align-items-center")
                    ], xs=4),
                ]),

    html.Br(),
    html.Footer('ABL',
            style={'textAlign': 'center', 
                'fontSize': 20, 
                'background-color':'#2a3f5f',
                'color':'white'})
    ], style={
        'paddingLeft':'10px',
        'paddingRight':'10px',
    })

#### Callback Auto Update Chart & Data
@callback(
    [
    Output('annual_ba_bar', 'figure'),
    Output('data_annual_ba_alerts', 'data'),
    Output('data_annual_ba_alerts', 'tooltip_data'),

    Output('special_ba_bar', 'figure'),
    Output('data_special_ba_alerts', 'data'),
    Output('data_special_ba_alerts', 'tooltip_data'),

    Output('intermediate_ba_bar', 'figure'),
    Output('data_intermediate_ba_alerts', 'data'),
    Output('data_intermediate_ba_alerts', 'tooltip_data'),

    Output('docking_ba_bar', 'figure'),
    Output('data_docking_ba_alerts', 'data'),
    Output('data_docking_ba_alerts', 'tooltip_data'),
    ],
    Input('store', 'data')
)
def update_charts(data):
    ######################
    # Pre Processing
    ######################
    df_ba = pd.DataFrame(data['Barge'])
    df_ba = df_ba.replace(r'^\s*$', np.nan, regex=True)
    date_ba = ['Keel Laying',
           'Annual Survey Last Date', 'Annual Survey Due Date',
           'Special Survey Last Date', 'Special Survey Due Date',
           'Intermediate Survey Last Date', 'Intermediate Survey Due Date',
           'Docking Survey Last Date', 'Docking Survey Due Date',] 
    df_ba[date_ba] = df_ba[date_ba].apply(pd.to_datetime, format='%d/%m/%Y')

    # New dataframe for remaining days
    diff_ba = ['Annual Survey Due Date', 'Special Survey Due Date', 'Intermediate Survey Due Date', 'Docking Survey Due Date']
    df_diff_ba = df_ba[['Barge Name']+diff_ba].copy()

    # Add new variable for remaining days
    diff_ba_name = ['Annual Survey Remain Days', 'Special Survey Remain Days', 'Intermediate Survey Remain Days', 'Docking Survey Remain Days']

    for (i,j) in zip(diff_ba, diff_ba_name):
        df_diff_ba[j] = (df_diff_ba[i]-pd.to_datetime('today')).dt.days

    # Add new variable for remaining days (Months, Days)
    diff_ba_name2 = ['Annual Survey Remain Days2', 'Special Survey Remain Days2', 'Intermediate Survey Remain Days2', 'Docking Survey Remain Days2']

    # Function for calculating remaining days
    def date_diff(var):
        remaining =[]
        for i in var:
            if i is pd.NaT:
                remaining.append(pd.Timestamp('NaT'))
            else :
                delta = relativedelta(i, pd.to_datetime('today'))
                res_months = delta.months + (delta.years * 12)
                remaining.append((str(res_months)+ ' months, '+ str(delta.days)+ ' days'))
        return(remaining)

    for i,j in zip(diff_ba, diff_ba_name2):
        df_diff_ba[j] = date_diff(df_diff_ba[i])
    
    # Add Last Date to DataFrame
    last_ba = ['Annual Survey Last Date', 'Special Survey Last Date', 'Intermediate Survey Last Date', 'Docking Survey Last Date']
    df_last_ba = pd.concat([df_diff_ba.copy(), df_ba[last_ba]], axis=1)
    
    ## DataFrame For Classification
    annual_ba_expired, annual_ba_alerts, annual_ba_ok = annual_classify(df_last_ba)
    special_ba_expired, special_ba_alerts, special_ba_ok = special_classify(df_last_ba)
    intermediate_ba_expired, intermediate_ba_alerts, intermediate_ba_ok = intermediate_classify(df_last_ba)
    docking_ba_expired, docking_ba_alerts, docking_ba_ok = docking_classify(df_last_ba)
    
    ## DataFrame to dash table
    data_annual_ba_alerts = annual_ba_alerts.to_dict('records')
    tooltip_annual_ba_alerts = tooltip_table(annual_ba_alerts)

    data_special_ba_alerts = special_ba_alerts.to_dict('records')
    tooltip_special_ba_alerts = tooltip_table(special_ba_alerts)

    data_intermediate_ba_alerts = intermediate_ba_alerts.to_dict('records')
    tooltip_intermediate_ba_alerts = tooltip_table(intermediate_ba_alerts)

    data_docking_ba_alerts = docking_ba_alerts.to_dict('records')
    tooltip_docking_ba_alerts = tooltip_table(docking_ba_alerts)

    ## DataFrame to Bar Plot data
    len_annual_ba = [len(annual_ba_ok), len(annual_ba_alerts), len(annual_ba_expired)]
    len_special_ba = [len(special_ba_ok), len(special_ba_alerts), len(special_ba_expired)]
    len_intermediate_ba = [len(intermediate_ba_ok), len(intermediate_ba_alerts), len(intermediate_ba_expired)]
    len_docking_ba = [len(docking_ba_ok), len(docking_ba_alerts), len(docking_ba_expired)]
    condition = ['Ok', 'Alerts', 'Expired']

    ## Barplot summary
    annual_ba_bar = bar_plot(len_annual_ba, condition)
    special_ba_bar = bar_plot(len_special_ba, condition)
    intermediate_ba_bar = bar_plot(len_intermediate_ba, condition)
    docking_ba_bar = bar_plot(len_docking_ba, condition)
    
    return annual_ba_bar, data_annual_ba_alerts, tooltip_annual_ba_alerts,\
            special_ba_bar, data_special_ba_alerts, tooltip_special_ba_alerts,\
            intermediate_ba_bar, data_intermediate_ba_alerts, tooltip_intermediate_ba_alerts,\
            docking_ba_bar, data_docking_ba_alerts, tooltip_docking_ba_alerts,\

######################
# Plot Function
######################
## 1. Annual
def annual_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['Annual Survey Remain Days'])) :
        if df['Annual Survey Remain Days'][i] < 0 :
            expired = expired.append({'Barge': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Annual Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Annual Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Annual Survey Due Date'][i]}, ignore_index=True)
        elif df['Annual Survey Remain Days'][i] < 92 :
            alerts = alerts.append({'Barge': df.iloc[:,0][i],
                                     'Remaining Days': df.loc[:,'Annual Survey Remain Days2'][i],
                                     'Last Date': df.loc[:,'Annual Survey Last Date'][i], 
                                     'Due Date': df.loc[:,'Annual Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Barge': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Annual Survey Remain Days2'][i],
                            'Last Date': df.loc[:,'Annual Survey Last Date'][i], 
                            'Due Date': df.loc[:,'Annual Survey Due Date'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 2. Special
def special_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['Special Survey Remain Days'])) :
        if df['Special Survey Remain Days'][i] < 0 :
            expired = expired.append({'Barge': df.iloc[:,0][i],
                                      'Remaining Days': df.loc[:,'Special Survey Remain Days2'][i],
                                      'Last Date': df.loc[:,'Special Survey Last Date'][i], 
                                      'Due Date': df.loc[:,'Special Survey Due Date'][i]}, ignore_index=True)
        elif df['Special Survey Remain Days'][i] < 183 :
            alerts = alerts.append({'Barge': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Special Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Special Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Special Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Barge': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Special Survey Remain Days2'][i],
                            'Last Date': df.loc[:,'Special Survey Last Date'][i], 
                            'Due Date': df.loc[:,'Special Survey Due Date'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 3. Intermediate
def intermediate_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['Intermediate Survey Remain Days'])) :
        if df['Intermediate Survey Remain Days'][i] < 0 :
            expired = expired.append({'Barge': df.iloc[:,0][i],
                                      'Remaining Days': df.loc[:,'Intermediate Survey Remain Days2'][i],
                                      'Last Date': df.loc[:,'Intermediate Survey Last Date'][i], 
                                      'Due Date': df.loc[:,'Intermediate Survey Due Date'][i]}, ignore_index=True)
        elif df['Intermediate Survey Remain Days'][i] < 183 :
            alerts = alerts.append({'Barge': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Intermediate Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Intermediate Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Intermediate Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Barge': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Intermediate Survey Remain Days2'][i],
                            'Last Date': df.loc[:,'Intermediate Survey Last Date'][i], 
                            'Due Date': df.loc[:,'Intermediate Survey Due Date'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 4. Docking
def docking_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['Docking Survey Remain Days'])) :
        if df['Docking Survey Remain Days'][i] < 0 :
            expired = expired.append({'Barge': df.iloc[:,0][i],
                                      'Remaining Days': df.loc[:,'Docking Survey Remain Days2'][i],
                                      'Last Date': df.loc[:,'Docking Survey Last Date'][i], 
                                      'Due Date': df.loc[:,'Docking Survey Due Date'][i]}, ignore_index=True)
        elif df['Docking Survey Remain Days'][i] < 183 :
            alerts = alerts.append({'Barge': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Docking Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Docking Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Docking Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Barge': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Docking Survey Remain Days2'][i],
                            'Last Date': df.loc[:,'Docking Survey Last Date'][i], 
                            'Due Date': df.loc[:,'Docking Survey Due Date'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 6. Bar Plot
def bar_plot(len, condition) :
    fig = go.Figure(go.Bar(y=len,
                            x=condition,
                            text=len,
                            marker_color=['#02b875','#f0ad4e','#d9534f']))
    fig.update_layout({'height':185, 
                        'width':160,
                        'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                        'margin' : {'t':3, 'b':3, 'l':3, 'r':3}})

    return fig

## 7. Tooltip
def tooltip_table(df):
    if df.empty == True :
        tooltip = []
    else :
        df['Last Date'] = df['Last Date'].dt.strftime('%d/%m/%Y')
        df['Due Date'] =  df['Due Date'].dt.strftime('%d/%m/%Y')
        tooltip =[{
            'Remaining Days': {'value': 'Last Date: {}  \n Due Date: {}'.format(row['Last Date'], row['Due Date']), 'type': 'markdown'},
        } for row in df.to_dict('records')]
    return tooltip




    