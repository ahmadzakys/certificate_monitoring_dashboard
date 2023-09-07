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

dash.register_page(__name__,  path='/', name='Status') # '/' is home page

##-----page 1

## -----LAYOUT-----
layout = html.Div([
                html.Br(),
                        html.P(children=[html.Strong('ABL FLEET CLASS STATUS')], 
                               style={'textAlign': 'center', 'fontSize': 27, 'background-color':'white','color':'#2a3f5f','font-family':'Verdana'}),
                ## --ROW1--
                dbc.Row([
                    html.Div(dash_table.DataTable(
                        id="data_dashboard",
                        columns=[{'name':['VESSEL','TYPE'],'id': 'level_0'},
                                 {'name':['VESSEL','VESSEL NAME'],'id': 'Vessel Name'},
                                 {'name':['VESSEL','CLASS'],'id': 'Class'},
                                 {'name':['CLASS SURVEY','ANNUAL'],'id': 'Annual'},
                                 {'name':['CLASS SURVEY','SPECIAL'],'id': 'Special'},
                                 {'name':['CLASS SURVEY','INTERMEDIATE'],'id': 'Intermediate'},
                                 {'name':['CLASS SURVEY','DOCKING'],'id': 'Docking'},
                                 {'name':['CLASS SURVEY','TAIL SHAFT'],'id': 'Tail Shaft'},
                                 {'name':['CLASS SURVEY','BOILER'],'id': 'Boiler'},
                                 {'name':['CLASS SURVEY','COC'],'id': 'COC'},],
                        merge_duplicate_headers=True,
                        # style_as_list_view=True,
                        style_header={'backgroundColor': '#2a3f5f',
                                    'fontWeight': 'bold',
                                    'color':'white',
                                    'border': '1px solid white'
                                },
                        style_cell_conditional=[{'if': {'column_id': 'Vessel Name'},
                                                'width': '19%'},
                                                {'if': {'column_id': 'level_0'},
                                                'width': '9%'},
                                                {'if': {'column_id': 'Class'},
                                                'width': '9%'},
                                                {'if': {'column_id': 'Annual'},
                                                'width': '9%'},
                                                {'if': {'column_id': 'Special'},
                                                'width': '9%'},
                                                {'if': {'column_id': 'Intermediate'},
                                                'width': '9%'},
                                                {'if': {'column_id': 'Docking'},
                                                'width': '9%'},
                                                {'if': {'column_id': 'Tail Shaft'},
                                                'width': '9%'},
                                                {'if': {'column_id': 'Boiler'},
                                                'width': '9%'},
                                                {'if': {'column_id': 'COC'},
                                                'width': '9%'},
                                                {'textAlign': 'center'}
                                                ],
                        style_cell={'font-family':'Verdana',
                                    'fontSize': 13,
                                    'color':'#2a3f5f',},
                        style_data_conditional=[{'if': {'column_id': 'level_0',},
                                                'fontWeight': 'bold'},
                                                {'if': {'filter_query': '{level_0} eq "CTS" || {level_0} eq "Barge"',
                                                        'column_id': ['Vessel Name','level_0','Class','Annual','Special','Intermediate','Docking','Tail Shaft','Boiler','COC']},
                                                'backgroundColor': '#F8F6F0',},
                                                ],
                        css=[{
                            'selector': '.dash-table-tooltip',
                            'rule': 'background-color: white; font-family: Verdana; color: #2a3f5f;'}],
                        tooltip_delay=0,
                        tooltip_duration=None
                    ))
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
    Output('data_dashboard', 'data'),
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
            'Boiler Survey Last Date', 'Boiler Survey Due Date',
            'COC Finding Date', 'COC Due Date'] 
    df_mv[date_mv] = df_mv[date_mv].apply(pd.to_datetime, format='%d/%m/%Y')

    df_cts = pd.DataFrame(data['Floating Crane'])
    df_cts = df_cts.replace(r'^\s*$', np.nan, regex=True)
    date_cts = ['Keel Laying', 'Year of Build', 
            'Annual Survey Last Date', 'Annual Survey Due Date', 
            'Special Survey Last Date', 'Special Survey Due Date',
            'Intermediate Survey Last Date', 'Intermediate Survey Due Date',
            'Docking Survey Last Date', 'Docking Survey Due Date',
            'Cargo Gear Survey Last Date', 'Cargo Gear Survey Due Date',
            'COC Finding Date', 'COC Due Date'] 
    df_cts[date_cts] = df_cts[date_cts].apply(pd.to_datetime, format='%d/%m/%Y')

    df_tb = pd.DataFrame(data['Tugboat'])
    df_tb = df_tb.replace(r'^\s*$', np.nan, regex=True)
    date_tb = ['Keel Laying', 'Year of Build', 
            'Annual Survey Last Date', 'Annual Survey Due Date',
            'Special Survey Last Date', 'Special Survey Due Date',
            'Intermediate Survey Last Date', 'Intermediate Survey Due Date',
            'Docking Survey Last Date', 'Docking Survey Due Date',
            'Tail Shaft Survey Last Date', 'Tail Shaft Survey Due Date',
            'COC Finding Date', 'COC Due Date'] 
    df_tb[date_tb] = df_tb[date_tb].apply(pd.to_datetime, format='%d/%m/%Y')

    df_ba = pd.DataFrame(data['Barge'])
    df_ba = df_ba.replace(r'^\s*$', np.nan, regex=True)
    date_ba = ['Keel Laying', 
            'Annual Survey Last Date', 'Annual Survey Due Date',
            'Special Survey Last Date', 'Special Survey Due Date',
            'Intermediate Survey Last Date', 'Intermediate Survey Due Date',
            'Docking Survey Last Date', 'Docking Survey Due Date',
            'COC Finding Date', 'COC Due Date'] 
    df_ba[date_ba] = df_ba[date_ba].apply(pd.to_datetime, format='%d/%m/%Y')

    # New dataframe for remaining days
    diff_mv = ['Annual Survey Due Date', 'Special Survey Due Date', 'Intermediate Survey Due Date', 'Docking Survey Due Date', 'Tail Shaft Survey Due Date', 'Boiler Survey Due Date', 'COC Due Date']
    df_diff_mv = df_mv[['Mother Vessel Name', 'Class']+diff_mv].copy()

    diff_cts = ['Annual Survey Due Date', 'Special Survey Due Date', 'Intermediate Survey Due Date', 'Docking Survey Due Date', 'Cargo Gear Survey Due Date', 'COC Due Date']
    df_diff_cts = df_cts[['CTS Name', 'Class']+diff_cts].copy()

    diff_tb = ['Annual Survey Due Date', 'Special Survey Due Date', 'Intermediate Survey Due Date', 'Docking Survey Due Date', 'Tail Shaft Survey Due Date', 'COC Due Date']
    df_diff_tb = df_tb[['Tugboat Name', 'Class']+diff_tb].copy()

    diff_ba = ['Annual Survey Due Date', 'Special Survey Due Date', 'Intermediate Survey Due Date', 'Docking Survey Due Date', 'COC Due Date']
    df_diff_ba = df_ba[['Barge Name', 'Class']+diff_ba].copy()

    # Add new variable for remaining days
    diff_mv_name = ['Annual Survey Remain Days', 'Special Survey Remain Days', 'Intermediate Survey Remain Days', 'Docking Survey Remain Days', 'Tail Shaft Survey Remain Days', 'Boiler Survey Remain Days', 'COC Remain Days']
    diff_cts_name = ['Annual Survey Remain Days', 'Special Survey Remain Days', 'Intermediate Survey Remain Days', 'Docking Survey Remain Days', 'Cargo Gear Survey Remain Days', 'COC Remain Days']
    diff_tb_name = ['Annual Survey Remain Days', 'Special Survey Remain Days', 'Intermediate Survey Remain Days', 'Docking Survey Remain Days', 'Tail Shaft Survey Remain Days', 'COC Remain Days']
    diff_ba_name = ['Annual Survey Remain Days', 'Special Survey Remain Days', 'Intermediate Survey Remain Days', 'Docking Survey Remain Days', 'COC Remain Days']
    
    for (i,j) in zip(diff_mv, diff_mv_name):
        df_diff_mv[j] = (df_diff_mv[i]-pd.to_datetime('today')).dt.days
    
    for (i,j) in zip(diff_cts, diff_cts_name):
        df_diff_cts[j] = (df_diff_cts[i]-pd.to_datetime('today')).dt.days
    
    for (i,j) in zip(diff_tb, diff_tb_name):
        df_diff_tb[j] = (df_diff_tb[i]-pd.to_datetime('today')).dt.days
    
    for (i,j) in zip(diff_ba, diff_ba_name):
        df_diff_ba[j] = (df_diff_ba[i]-pd.to_datetime('today')).dt.days

    # Rename vessel name column
    df_diff_mv = df_diff_mv.rename(columns={'Mother Vessel Name':'Vessel Name'})
    df_diff_cts = df_diff_cts.rename(columns={'CTS Name':'Vessel Name'})
    df_diff_tb = df_diff_tb.rename(columns={'Tugboat Name':'Vessel Name'})
    df_diff_ba = df_diff_ba.rename(columns={'Barge Name':'Vessel Name'})

    # Add emoji symbol for alerts
    df_diff_mv['Annual'] = df_diff_mv['Annual Survey Remain Days'].apply(lambda x:
                                                                         '❌' if x < 0 else (
                                                                             '⚠️' if x < 92 else '✔️'))
    old_mv = ['Special Survey Remain Days', 'Intermediate Survey Remain Days', 'Docking Survey Remain Days', 'Tail Shaft Survey Remain Days', 'Boiler Survey Remain Days', 'COC Remain Days']
    new_mv = ['Special', 'Intermediate', 'Docking', 'Tail Shaft', 'Boiler', 'COC']
    for i,j in zip(new_mv, old_mv):
        df_diff_mv[i] = df_diff_mv[j].apply(lambda x:
                                            '❌' if x < 0 else (
                                            '⚠️' if x < 183 else '✔️'))
        
    df_diff_cts['Annual'] = df_diff_cts['Annual Survey Remain Days'].apply(lambda x:
                                                                         '❌' if x < 0 else (
                                                                             '⚠️' if x < 92 else '✔️'))
    old_cts = ['Special Survey Remain Days', 'Intermediate Survey Remain Days', 'Docking Survey Remain Days', 'COC Remain Days']
    new_cts = ['Special', 'Intermediate', 'Docking', 'COC']
    for i,j in zip(new_cts, old_cts):
        df_diff_cts[i] = df_diff_cts[j].apply(lambda x:
                                            '❌' if x < 0 else (
                                            '⚠️' if x < 183 else '✔️'))
        
    df_diff_tb['Annual'] = df_diff_tb['Annual Survey Remain Days'].apply(lambda x:
                                                                         '❌' if x < 0 else (
                                                                             '⚠️' if x < 92 else '✔️'))
    old_tb = ['Special Survey Remain Days', 'Intermediate Survey Remain Days', 'Docking Survey Remain Days', 'Tail Shaft Survey Remain Days', 'COC Remain Days']
    new_tb = ['Special', 'Intermediate', 'Docking', 'Tail Shaft', 'COC']
    for i,j in zip(new_tb, old_tb):
        df_diff_tb[i] = df_diff_tb[j].apply(lambda x:
                                            '❌' if x < 0 else (
                                            '⚠️' if x < 183 else '✔️'))
        
    df_diff_ba['Annual'] = df_diff_ba['Annual Survey Remain Days'].apply(lambda x:
                                                                         '❌' if x < 0 else (
                                                                             '⚠️' if x < 92 else '✔️'))
    old_ba = ['Special Survey Remain Days', 'Intermediate Survey Remain Days', 'Docking Survey Remain Days', 'COC Remain Days']
    new_ba = ['Special', 'Intermediate', 'Docking', 'COC']
    for i,j in zip(new_ba, old_ba):
        df_diff_ba[i] = df_diff_ba[j].apply(lambda x:
                                            '❌' if x < 0 else (
                                            '⚠️' if x < 183 else '✔️'))

    data_mv = df_diff_mv[['Vessel Name', 'Class', 'Annual', 'Special', 'Intermediate', 'Docking', 'Tail Shaft', 'Boiler', 'COC']]
    data_cts = df_diff_cts[['Vessel Name', 'Class', 'Annual', 'Special', 'Intermediate', 'Docking', 'COC']]
    data_tb = df_diff_tb[['Vessel Name', 'Class', 'Annual', 'Special', 'Intermediate', 'Docking', 'Tail Shaft', 'COC']]
    data_ba = df_diff_ba[['Vessel Name', 'Class', 'Annual', 'Special', 'Intermediate', 'Docking', 'COC']]
    data = pd.concat([data_mv, data_cts, data_tb, data_ba], keys=['OGV', 'CTS', 'Tugboat', 'Barge'])
    data = data.fillna('🔲').reset_index()
    
        
    ## DataFrame to dash table
    data_dashboard = [data.to_dict('records')]
    
    return data_dashboard


