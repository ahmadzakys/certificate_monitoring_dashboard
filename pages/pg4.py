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

dash.register_page(__name__, name='Tugboat') # '/' is home page

##-----page 4

## -----LAYOUT-----
layout = html.Div([
                html.Br(),
                        html.P(children=[html.Strong('Tugboat')], 
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
                                    dbc.CardBody(dcc.Graph(id='annual_tb_bar3'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### Annual Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_annual_tb_alerts3",
                                                                               columns=[{'name':'Tugboat','id': 'Tugboat'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'Tugboat'},
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
                                                                                   'rule': 'background-color: grey; font-family: monospace; color: white',
                                                                                #    'rule': 'background-color: white; font-family: monospace; color: #2a3f5f;',
                                                                                   }],
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
                                    dbc.CardBody(dcc.Graph(id='special_tb_bar3'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### Special Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_special_tb_alerts3",
                                                                               columns=[{'name':'Tugboat','id': 'Tugboat'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'Tugboat'},
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
                                    dbc.CardBody(dcc.Graph(id='intermediate_tb_bar3'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### Intermediate Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_intermediate_tb_alerts3",
                                                                               columns=[{'name':'Tugboat','id': 'Tugboat'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'Tugboat'},
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
                                    dbc.CardBody(dcc.Graph(id='docking_tb_bar3'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### docking Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_docking_tb_alerts3",
                                                                               columns=[{'name':'Tugboat','id': 'Tugboat'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'Tugboat'},
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
                        html.P(children=[html.Strong('Tail Shaft Survey')], 
                               style={'textAlign': 'center', 'fontSize': 22, 'background-color':'white','color':'#2a3f5f','font-family':'Verdana'}),

                        dbc.Row([###### Tail Shaft Summary
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
                            ###### Tail Shaft Alerts
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
                            ###### Tail Shaft Bar Plot
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(dcc.Graph(id='tail_shaft_tb_bar3'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### Tail Shaft Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_tail_shaft_tb_alerts3",
                                                                               columns=[{'name':'Tugboat','id': 'Tugboat'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'Tugboat'},
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
    Output('annual_tb_bar3', 'figure'),
    Output('data_annual_tb_alerts3', 'data'),
    Output('data_annual_tb_alerts3', 'tooltip_data'),

    Output('special_tb_bar3', 'figure'),
    Output('data_special_tb_alerts3', 'data'),
    Output('data_special_tb_alerts3', 'tooltip_data'),

    Output('intermediate_tb_bar3', 'figure'),
    Output('data_intermediate_tb_alerts3', 'data'),
    Output('data_intermediate_tb_alerts3', 'tooltip_data'),

    Output('docking_tb_bar3', 'figure'),
    Output('data_docking_tb_alerts3', 'data'),
    Output('data_docking_tb_alerts3', 'tooltip_data'),

    Output('tail_shaft_tb_bar3', 'figure'),
    Output('data_tail_shaft_tb_alerts3', 'data'),
    Output('data_tail_shaft_tb_alerts3', 'tooltip_data'),
    ],
    Input('store', 'data')
)
def update_charts(data):
    ######################
    # Pre Processing
    ######################
    df_tb = pd.DataFrame(data['Tugboat'])
    df_tb = df_tb.replace(r'^\s*$', np.nan, regex=True)
    date_tb = ['Keel Laying', 'Year of Build', 
           'Annual Survey Last Date', 'Annual Survey Due Date',
           'Special Survey Last Date', 'Special Survey Due Date',
           'Intermediate Survey Last Date', 'Intermediate Survey Due Date',
           'Docking Survey Last Date', 'Docking Survey Due Date',
           'Tail Shaft Survey Last Date', 'Tail Shaft Survey Due Date',] 
    df_tb[date_tb] = df_tb[date_tb].apply(pd.to_datetime, format='%d/%m/%Y')

    # New dataframe for remaining days
    diff_tb = ['Annual Survey Due Date', 'Special Survey Due Date', 'Intermediate Survey Due Date', 'Docking Survey Due Date', 'Tail Shaft Survey Due Date']
    df_diff_tb = df_tb[['Tugboat Name', 'Call Sign']+diff_tb].copy()

    # Add new variable for remaining days
    diff_tb_name = ['Annual Survey Remain Days', 'Special Survey Remain Days', 'Intermediate Survey Remain Days', 'Docking Survey Remain Days', 'Tail Shaft Survey Remain Days']

    for (i,j) in zip(diff_tb, diff_tb_name):
        df_diff_tb[j] = (df_diff_tb[i]-pd.to_datetime('today')).dt.days

    # Add new variable for remaining days (Months, Days)
    diff_tb_name2 = ['Annual Survey Remain Days2', 'Special Survey Remain Days2', 'Intermediate Survey Remain Days2', 'Docking Survey Remain Days2', 'Tail Shaft Survey Remain Days2']

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

    for i,j in zip(diff_tb, diff_tb_name2):
        df_diff_tb[j] = date_diff(df_diff_tb[i])
    
    # Add Last Date to DataFrame
    last_tb = ['Annual Survey Last Date', 'Special Survey Last Date', 'Intermediate Survey Last Date', 'Docking Survey Last Date', 'Tail Shaft Survey Last Date']
    df_last_tb = pd.concat([df_diff_tb.copy(), df_tb[last_tb]], axis=1)
    
    ## DataFrame For Classification
    annual_tb_expired, annual_tb_alerts, annual_tb_ok = annual_classify(df_last_tb)
    special_tb_expired, special_tb_alerts, special_tb_ok = special_classify(df_last_tb)
    intermediate_tb_expired, intermediate_tb_alerts, intermediate_tb_ok = intermediate_classify(df_last_tb)
    docking_tb_expired, docking_tb_alerts, docking_tb_ok = docking_classify(df_last_tb)
    tail_shaft_tb_expired, tail_shaft_tb_alerts, tail_shaft_tb_ok = tail_shaft_classify(df_last_tb)
    
    ## DataFrame to dash table
    data_annual_tb_alerts = annual_tb_alerts.to_dict('records')
    tooltip_annual_tb_alerts = tooltip_table(annual_tb_alerts)

    data_special_tb_alerts = special_tb_alerts.to_dict('records')
    tooltip_special_tb_alerts = tooltip_table(special_tb_alerts)

    data_intermediate_tb_alerts = intermediate_tb_alerts.to_dict('records')
    tooltip_intermediate_tb_alerts = tooltip_table(intermediate_tb_alerts)

    data_docking_tb_alerts = docking_tb_alerts.to_dict('records')
    tooltip_docking_tb_alerts = tooltip_table(docking_tb_alerts)

    data_tail_shaft_tb_alerts = tail_shaft_tb_alerts.to_dict('records')
    tooltip_tail_shaft_tb_alerts = tooltip_table(tail_shaft_tb_alerts)

    ## DataFrame to Bar Plot data
    len_annual_tb = [len(annual_tb_ok), len(annual_tb_alerts), len(annual_tb_expired)]
    len_special_tb = [len(special_tb_ok), len(special_tb_alerts), len(special_tb_expired)]
    len_intermediate_tb = [len(intermediate_tb_ok), len(intermediate_tb_alerts), len(intermediate_tb_expired)]
    len_docking_tb = [len(docking_tb_ok), len(docking_tb_alerts), len(docking_tb_expired)]
    len_tail_shaft_tb = [len(tail_shaft_tb_ok), len(tail_shaft_tb_alerts), len(tail_shaft_tb_expired)]
    condition = ['Ok', 'Alerts', 'Expired']

    ## Barplot summary
    annual_tb_bar3 = bar_plot(len_annual_tb, condition)
    special_tb_bar3 = bar_plot(len_special_tb, condition)
    intermediate_tb_bar3 = bar_plot(len_intermediate_tb, condition)
    docking_tb_bar3 = bar_plot(len_docking_tb, condition)
    tail_shaft_tb_bar3 = bar_plot(len_tail_shaft_tb, condition)
    
    return annual_tb_bar3, data_annual_tb_alerts, tooltip_annual_tb_alerts,\
            special_tb_bar3, data_special_tb_alerts, tooltip_special_tb_alerts,\
            intermediate_tb_bar3, data_intermediate_tb_alerts, tooltip_intermediate_tb_alerts,\
            docking_tb_bar3, data_docking_tb_alerts, tooltip_docking_tb_alerts,\
            tail_shaft_tb_bar3, data_tail_shaft_tb_alerts, tooltip_tail_shaft_tb_alerts,


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
            expired = expired.append({'Tugboat': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Annual Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Annual Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Annual Survey Due Date'][i]}, ignore_index=True)
        elif df['Annual Survey Remain Days'][i] < 92 :
            alerts = alerts.append({'Tugboat': df.iloc[:,0][i],
                                     'Remaining Days': df.loc[:,'Annual Survey Remain Days2'][i],
                                     'Last Date': df.loc[:,'Annual Survey Last Date'][i], 
                                     'Due Date': df.loc[:,'Annual Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Tugboat': df.iloc[:,0][i],
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
            expired = expired.append({'Tugboat': df.iloc[:,0][i],
                                      'Remaining Days': df.loc[:,'Special Survey Remain Days2'][i],
                                      'Last Date': df.loc[:,'Special Survey Last Date'][i], 
                                      'Due Date': df.loc[:,'Special Survey Due Date'][i]}, ignore_index=True)
        elif df['Special Survey Remain Days'][i] < 183 :
            alerts = alerts.append({'Tugboat': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Special Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Special Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Special Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Tugboat': df.iloc[:,0][i],
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
            expired = expired.append({'Tugboat': df.iloc[:,0][i],
                                      'Remaining Days': df.loc[:,'Intermediate Survey Remain Days2'][i],
                                      'Last Date': df.loc[:,'Intermediate Survey Last Date'][i], 
                                      'Due Date': df.loc[:,'Intermediate Survey Due Date'][i]}, ignore_index=True)
        elif df['Intermediate Survey Remain Days'][i] < 183 :
            alerts = alerts.append({'Tugboat': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Intermediate Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Intermediate Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Intermediate Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Tugboat': df.iloc[:,0][i],
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
            expired = expired.append({'Tugboat': df.iloc[:,0][i],
                                      'Remaining Days': df.loc[:,'Docking Survey Remain Days2'][i],
                                      'Last Date': df.loc[:,'Docking Survey Last Date'][i], 
                                      'Due Date': df.loc[:,'Docking Survey Due Date'][i]}, ignore_index=True)
        elif df['Docking Survey Remain Days'][i] < 183 :
            alerts = alerts.append({'Tugboat': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Docking Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Docking Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Docking Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Tugboat': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Docking Survey Remain Days2'][i],
                            'Last Date': df.loc[:,'Docking Survey Last Date'][i], 
                            'Due Date': df.loc[:,'Docking Survey Due Date'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 5. Tail Shaft
def tail_shaft_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['Tail Shaft Survey Remain Days'])) :
        if df['Tail Shaft Survey Remain Days'][i] < 0 :
            expired = expired.append({'Tugboat': df.iloc[:,0][i],
                                      'Remaining Days': df.loc[:,'Tail Shaft Survey Remain Days2'][i],
                                      'Last Date': df.loc[:,'Tail Shaft Survey Last Date'][i], 
                                      'Due Date': df.loc[:,'Tail Shaft Survey Due Date'][i]}, ignore_index=True)
        elif df['Tail Shaft Survey Remain Days'][i] < 183 :
            alerts = alerts.append({'Tugboat': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Tail Shaft Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Tail Shaft Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Tail Shaft Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'Tugboat': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Tail Shaft Survey Remain Days2'][i],
                            'Last Date': df.loc[:,'Tail Shaft Survey Last Date'][i], 
                            'Due Date': df.loc[:,'Tail Shaft Survey Due Date'][i]}, ignore_index=True)
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
            'Remaining Days': {'value': 'Last Date: {}  \nDue Date: {}'.format(row['Last Date'], row['Due Date']), 'type': 'markdown', },
        } for row in df.to_dict('records')]
    return tooltip




    