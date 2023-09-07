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

dash.register_page(__name__,  name='OGV') # '/' is home page

##-----page 2

## -----LAYOUT-----
layout = html.Div([
                html.Br(),
                        html.P(children=[html.Strong('On Going Vessel')], 
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
                                    dbc.CardBody(dcc.Graph(id='annual_mv_bar'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### Annual Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_annual_mv_alerts",
                                                                               columns=[{'name':'OGV','id': 'OGV'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'OGV'},
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
                                    dbc.CardBody(dcc.Graph(id='special_mv_bar'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### Special Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_special_mv_alerts",
                                                                               columns=[{'name':'OGV','id': 'OGV'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'OGV'},
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
                                    dbc.CardBody(dcc.Graph(id='intermediate_mv_bar'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### Intermediate Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_intermediate_mv_alerts",
                                                                               columns=[{'name':'OGV','id': 'OGV'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'OGV'},
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
                                    dbc.CardBody(dcc.Graph(id='docking_mv_bar'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### docking Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_docking_mv_alerts",
                                                                               columns=[{'name':'OGV','id': 'OGV'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'OGV'},
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
                                    dbc.CardBody(dcc.Graph(id='tail_shaft_mv_bar'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### Tail Shaft Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_tail_shaft_mv_alerts",
                                                                               columns=[{'name':'OGV','id': 'OGV'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'OGV'},
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
                        ], className="g-0 d-flex align-items-center"),
                    ], xs=4),

                    dbc.Col([
                        html.Br(),
                        html.P(children=[html.Strong('Boiler Survey')], 
                               style={'textAlign': 'center', 'fontSize': 22, 'background-color':'white','color':'#2a3f5f','font-family':'Verdana'}),

                        dbc.Row([###### Boiler Summary
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
                            ###### Boiler Alerts
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
                            ###### Boiler Bar Plot
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(dcc.Graph(id='boiler_mv_bar'))
                                ], color="light", outline=True, style={"height": 210, "margin-bottom": "5px"}),
                            ], xs=5),
                            ###### Boiler Alerts Table
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody(html.Div(dash_table.DataTable(id="data_boiler_mv_alerts",
                                                                               columns=[{'name':'OGV','id': 'OGV'},
                                                                                        {'name':'Remaining Days','id': 'Remaining Days'}],
                                                                               style_as_list_view=True,
                                                                               style_header={'backgroundColor': 'white',
                                                                                            'fontWeight': 'bold'
                                                                                        },
                                                                               style_cell_conditional=[{'if': {'column_id': 'OGV'},
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
                        ], className="g-0 d-flex align-items-center"),
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
    Output('annual_mv_bar', 'figure'),
    Output('data_annual_mv_alerts', 'data'),
    Output('data_annual_mv_alerts', 'tooltip_data'),

    Output('special_mv_bar', 'figure'),
    Output('data_special_mv_alerts', 'data'),
    Output('data_special_mv_alerts', 'tooltip_data'),

    Output('intermediate_mv_bar', 'figure'),
    Output('data_intermediate_mv_alerts', 'data'),
    Output('data_intermediate_mv_alerts', 'tooltip_data'),

    Output('docking_mv_bar', 'figure'),
    Output('data_docking_mv_alerts', 'data'),
    Output('data_docking_mv_alerts', 'tooltip_data'),

    Output('tail_shaft_mv_bar', 'figure'),
    Output('data_tail_shaft_mv_alerts', 'data'),
    Output('data_tail_shaft_mv_alerts', 'tooltip_data'),

    Output('boiler_mv_bar', 'figure'),
    Output('data_boiler_mv_alerts', 'data'),
    Output('data_boiler_mv_alerts', 'tooltip_data'),
    ],
    Input('store', 'data')
)
def update_charts(data):
    ######################
    # Pre Processing
    ######################
    df_mv = pd.DataFrame(data['Mother Vessel'])
    df_mv = df_mv.replace(r'^\s*$', np.nan, regex=True)
    date_mv = ['Keel Laying', 'Year of Build', 
           'Annual Survey Last Date', 'Annual Survey Due Date',
           'Special Survey Last Date', 'Special Survey Due Date',
           'Intermediate Survey Last Date', 'Intermediate Survey Due Date',
           'Docking Survey Last Date', 'Docking Survey Due Date',
           'Tail Shaft Survey Last Date', 'Tail Shaft Survey Due Date',
           'Boiler Survey Last Date', 'Boiler Survey Due Date',] 
    df_mv[date_mv] = df_mv[date_mv].apply(pd.to_datetime, format='%d/%m/%Y')

    # New dataframe for remaining days
    diff_mv = ['Annual Survey Due Date', 'Special Survey Due Date', 'Intermediate Survey Due Date', 'Docking Survey Due Date', 'Tail Shaft Survey Due Date', 'Boiler Survey Due Date']
    df_diff_mv = df_mv[['Mother Vessel Name', 'Call Sign']+diff_mv].copy()

    # Add new variable for remaining days
    diff_mv_name = ['Annual Survey Remain Days', 'Special Survey Remain Days', 'Intermediate Survey Remain Days', 'Docking Survey Remain Days', 'Tail Shaft Survey Remain Days', 'Boiler Survey Remain Days']

    for (i,j) in zip(diff_mv, diff_mv_name):
        df_diff_mv[j] = (df_diff_mv[i]-pd.to_datetime('today')).dt.days

    # Add new variable for remaining days (Years, Months, Days)
    diff_mv_name2 = ['Annual Survey Remain Days2', 'Special Survey Remain Days2', 'Intermediate Survey Remain Days2', 'Docking Survey Remain Days2', 'Tail Shaft Survey Remain Days2', 'Boiler Survey Remain Days2']

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

    for i,j in zip(diff_mv, diff_mv_name2):
        df_diff_mv[j] = date_diff(df_diff_mv[i])
        
    # Add Last Date to DataFrame    
    last_mv = ['Annual Survey Last Date', 'Special Survey Last Date', 'Intermediate Survey Last Date', 'Docking Survey Last Date', 'Tail Shaft Survey Last Date', 'Boiler Survey Due Date']
    df_last_mv = pd.concat([df_diff_mv.copy(), df_mv[last_mv]], axis=1)
    
    
    ## DataFrame For Classification
    annual_mv_expired, annual_mv_alerts, annual_mv_ok = annual_classify(df_last_mv)
    special_mv_expired, special_mv_alerts, special_mv_ok = special_classify(df_last_mv)
    intermediate_mv_expired, intermediate_mv_alerts, intermediate_mv_ok = intermediate_classify(df_last_mv)
    docking_mv_expired, docking_mv_alerts, docking_mv_ok = docking_classify(df_last_mv)
    tail_shaft_mv_expired, tail_shaft_mv_alerts, tail_shaft_mv_ok = tail_shaft_classify(df_last_mv)
    boiler_mv_expired, boiler_mv_alerts, boiler_mv_ok = boiler_classify(df_last_mv)
    
    ## DataFrame to dash table
    data_annual_mv_alerts = annual_mv_alerts.to_dict('records')
    tooltip_annual_mv_alerts = tooltip_table(annual_mv_alerts)

    data_special_mv_alerts = special_mv_alerts.to_dict('records')
    tooltip_special_mv_alerts = tooltip_table(special_mv_alerts)

    data_intermediate_mv_alerts = intermediate_mv_alerts.to_dict('records')
    tooltip_intermediate_mv_alerts = tooltip_table(intermediate_mv_alerts)

    data_docking_mv_alerts = docking_mv_alerts.to_dict('records')
    tooltip_docking_mv_alerts = tooltip_table(docking_mv_alerts)

    data_tail_shaft_mv_alerts = tail_shaft_mv_alerts.to_dict('records')
    tooltip_tail_shaft_mv_alerts = tooltip_table(tail_shaft_mv_alerts)

    data_boiler_mv_alerts = boiler_mv_alerts.to_dict('records')
    tooltip_boiler_mv_alerts = tooltip_table(boiler_mv_alerts)

    ## DataFrame to Bar Plot data
    len_annual_mv = [len(annual_mv_ok), len(annual_mv_alerts), len(annual_mv_expired)]
    len_special_mv = [len(special_mv_ok), len(special_mv_alerts), len(special_mv_expired)]
    len_intermediate_mv = [len(intermediate_mv_ok), len(intermediate_mv_alerts), len(intermediate_mv_expired)]
    len_docking_mv = [len(docking_mv_ok), len(docking_mv_alerts), len(docking_mv_expired)]
    len_tail_shaft_mv = [len(tail_shaft_mv_ok), len(tail_shaft_mv_alerts), len(tail_shaft_mv_expired)]
    len_boiler_mv = [len(boiler_mv_ok), len(boiler_mv_alerts), len(boiler_mv_expired)]
    condition = ['Ok', 'Alerts', 'Expired']

    ## Barplot summary
    annual_mv_bar = bar_plot(len_annual_mv, condition)
    special_mv_bar = bar_plot(len_special_mv, condition)
    intermediate_mv_bar = bar_plot(len_intermediate_mv, condition)
    docking_mv_bar = bar_plot(len_docking_mv, condition)
    tail_shaft_mv_bar = bar_plot(len_tail_shaft_mv, condition)
    boiler_mv_bar = bar_plot(len_boiler_mv, condition)
    
    return annual_mv_bar, data_annual_mv_alerts, tooltip_annual_mv_alerts,\
            special_mv_bar, data_special_mv_alerts, tooltip_special_mv_alerts,\
            intermediate_mv_bar, data_intermediate_mv_alerts, tooltip_intermediate_mv_alerts,\
            docking_mv_bar, data_docking_mv_alerts, tooltip_docking_mv_alerts,\
            tail_shaft_mv_bar, data_tail_shaft_mv_alerts, tooltip_tail_shaft_mv_alerts,\
            boiler_mv_bar, data_boiler_mv_alerts, tooltip_boiler_mv_alerts,


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
            expired = expired.append({'OGV': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Annual Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Annual Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Annual Survey Due Date'][i]}, ignore_index=True)
        elif df['Annual Survey Remain Days'][i] < 92 :
            alerts = alerts.append({'OGV': df.iloc[:,0][i],
                                     'Remaining Days': df.loc[:,'Annual Survey Remain Days2'][i],
                                     'Last Date': df.loc[:,'Annual Survey Last Date'][i], 
                                     'Due Date': df.loc[:,'Annual Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'OGV': df.iloc[:,0][i],
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
            expired = expired.append({'OGV': df.iloc[:,0][i],
                                      'Remaining Days': df.loc[:,'Special Survey Remain Days2'][i],
                                      'Last Date': df.loc[:,'Special Survey Last Date'][i], 
                                      'Due Date': df.loc[:,'Special Survey Due Date'][i]}, ignore_index=True)
        elif df['Special Survey Remain Days'][i] < 183 :
            alerts = alerts.append({'OGV': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Special Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Special Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Special Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'OGV': df.iloc[:,0][i],
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
            expired = expired.append({'OGV': df.iloc[:,0][i],
                                      'Remaining Days': df.loc[:,'Intermediate Survey Remain Days2'][i],
                                      'Last Date': df.loc[:,'Intermediate Survey Last Date'][i], 
                                      'Due Date': df.loc[:,'Intermediate Survey Due Date'][i]}, ignore_index=True)
        elif df['Intermediate Survey Remain Days'][i] < 183 :
            alerts = alerts.append({'OGV': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Intermediate Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Intermediate Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Intermediate Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'OGV': df.iloc[:,0][i],
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
            expired = expired.append({'OGV': df.iloc[:,0][i],
                                      'Remaining Days': df.loc[:,'Docking Survey Remain Days2'][i],
                                      'Last Date': df.loc[:,'Docking Survey Last Date'][i], 
                                      'Due Date': df.loc[:,'Docking Survey Due Date'][i]}, ignore_index=True)
        elif df['Docking Survey Remain Days'][i] < 183 :
            alerts = alerts.append({'OGV': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Docking Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Docking Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Docking Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'OGV': df.iloc[:,0][i],
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
            expired = expired.append({'OGV': df.iloc[:,0][i],
                                      'Remaining Days': df.loc[:,'Tail Shaft Survey Remain Days2'][i],
                                      'Last Date': df.loc[:,'Tail Shaft Survey Last Date'][i], 
                                      'Due Date': df.loc[:,'Tail Shaft Survey Due Date'][i]}, ignore_index=True)
        elif df['Tail Shaft Survey Remain Days'][i] < 183 :
            alerts = alerts.append({'OGV': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Tail Shaft Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Tail Shaft Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Tail Shaft Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'OGV': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Tail Shaft Survey Remain Days2'][i],
                            'Last Date': df.loc[:,'Tail Shaft Survey Last Date'][i], 
                            'Due Date': df.loc[:,'Tail Shaft Survey Due Date'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 6. Boiler
def boiler_classify(df):
    
    expired = pd.DataFrame()
    alerts = pd.DataFrame()
    ok = pd.DataFrame()

    for i in range(len(df['Boiler Survey Remain Days'])) :
        if df['Boiler Survey Remain Days'][i] < 0 :
            expired = expired.append({'OGV': df.iloc[:,0][i],
                                      'Remaining Days': df.loc[:,'Docking Survey Remain Days2'][i],
                                      'Last Date': df.loc[:,'Docking Survey Last Date'][i], 
                                      'Due Date': df.loc[:,'Docking Survey Due Date'][i]}, ignore_index=True)
        elif df['Boiler Survey Remain Days'][i] < 183 :
            alerts = alerts.append({'OGV': df.iloc[:,0][i],
                                    'Remaining Days': df.loc[:,'Docking Survey Remain Days2'][i],
                                    'Last Date': df.loc[:,'Docking Survey Last Date'][i], 
                                    'Due Date': df.loc[:,'Docking Survey Due Date'][i]}, ignore_index=True)
        else :
            ok = ok.append({'OGV': df.iloc[:,0][i],
                            'Remaining Days': df.loc[:,'Docking Survey Remain Days2'][i],
                            'Last Date': df.loc[:,'Docking Survey Last Date'][i], 
                            'Due Date': df.loc[:,'Docking Survey Due Date'][i]}, ignore_index=True)
    return(expired, alerts, ok)

## 7. Bar Plot
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

## 8. Tooltip
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




    