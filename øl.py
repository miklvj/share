# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:57:02 2022

@author: mikke
"""


import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go
import numpy
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output





'''
PLUG IN STATS
'''





navn = ['Punk IPA', 'Aarhus Tribute', 'Santa Gose', 'Red Noses', 'Christmas Ale', 'Yule Juice', 'Yuzual Suspect', 'Hazy Jane', 'No.5 Valnød', 'Snug as a Bug in a Rug', 'Santas Hoppy Helpers']
bryggeri = ['Brewdog', 'Aarhus Bryghus', 'To Øl', 'Anarkist', 'Jacobsen', 'Amager Bryghus', 'To Øl', 'Brewdog', 'Ærø Bryghus', 'Salikatt', 'Mikkeller']
type = ['IPA', 'Barleywine', 'Sour', 'Red Ale', 'Red Ale', 'IPA', 'Sour', 'IPA', 'Bock', 'NEIPA', 'IPA']
procent = [5.4, 9.0, 4.0, 5.5, 7.5, 6.5, 4.5, 5.0, 7.0, 8.0, 6.0]


'''
Ems
'''

duft_ems = [4, 4, 5, 2, 4, 5, 1, 3, 2, 4, 3]
smag_ems = [8, 6, 9, 4, 7, 6, 6, 6, 5, 8, 7]
helhedsoplevelse_ems = [4, 3, 5, 2, 3, 4, 4, 3, 2, 4, 4]


'''
Tejl
'''

duft_tejl = [5, 2, 4, 2, 4, 4, 1, 2, 4, 5, 5]
smag_tejl = [7, 9, 7, 5, 7, 6, 8, 6, 6, 9, 8]
helhedsoplevelse_tejl = [4, 3, 4, 3, 4, 2, 4, 3, 3, 5, 5]


'''
Miks
'''

duft_miks = [3, 4, 4, 2, 3, 5, 3, 2, 3, 4, 3]
smag_miks = [7, 6, 9, 4, 6, 7, 9, 5, 4, 7, 7]
helhedsoplevelse_miks = [3, 3, 5, 2, 3, 3, 5, 3, 2, 4, 4]





'''
CHECK LENGTH
'''





print(len(duft_tejl))
print(len(duft_ems))
print(len(duft_miks))

print(len(smag_tejl))
print(len(smag_ems))
print(len(smag_miks))

print(len(helhedsoplevelse_tejl))
print(len(helhedsoplevelse_ems))
print(len(helhedsoplevelse_miks))


print(len(type))
print(len(navn))
print(len(bryggeri))
print(len(procent))





'''
CREATE DF
'''





df = pd.DataFrame(list(zip(navn,
                           bryggeri, 
                           type, 
                           procent, 
                           duft_ems, 
                           duft_tejl, 
                           duft_miks, 
                           smag_ems, 
                           smag_tejl, 
                           smag_miks, 
                           helhedsoplevelse_ems, 
                           helhedsoplevelse_tejl, 
                           helhedsoplevelse_miks)))



columns_names = ['navn', 
                 'bryggeri',
                 'type',
                 'procent',
                 'duft_ems',
                 'duft_tejl',
                 'duft_miks',
                 'smag_ems',
                 'smag_tejl',
                 'smag_miks',
                 'helhedsoplevelse_ems',
                 'helhedsoplevelse_tejl',
                 'helhedsoplevelse_miks']


df.columns = columns_names #APPEND THE COLUMN NAMES^





'''
MODIFY DF
'''





#CREATE COLUMNS FOR SMAG WITH SAME SCALE = 5
smag_ems_div = [] 
for i in df['smag_ems'].values:
    value_div = i/2
    smag_ems_div.append(value_div)
df['smag_ems_div'] = smag_ems_div

smag_tejl_div = [] 
for i in df['smag_tejl'].values:
    value_div = i/2
    smag_tejl_div.append(value_div)
df['smag_tejl_div'] = smag_tejl_div

smag_miks_div = [] 
for i in df['smag_miks'].values:
    value_div = i/2
    smag_miks_div.append(value_div)
df['smag_miks_div'] = smag_miks_div




#CREATE A COLUMN WITH TOTAL SMAG
ems_smag = []
tejl_smag = []
miks_smag = []
for i in df['smag_ems'].values:
    ems_smag.append(i)
for i in df['smag_tejl'].values:
    tejl_smag.append(i)
for i in df['smag_miks'].values:
    miks_smag.append(i)
smag_total = list(map(sum, zip(ems_smag,tejl_smag,miks_smag)))
df['smag_total'] = smag_total




#CREATE A COLUMN WITH TOTAL DUFT
ems_duft = []
tejl_duft = []
miks_duft = []
for i in df['duft_ems'].values:
    ems_duft.append(i)
for i in df['duft_tejl'].values:
    tejl_duft.append(i)
for i in df['duft_miks'].values:
    miks_duft.append(i)
duft_total = list(map(sum, zip(ems_duft,tejl_duft,miks_duft)))
df['duft_total'] = duft_total   




#CREATE A COLUMN WITH TOTAL HELHEDSOPLEVELSE
ems_helhedsoplevelse = []
tejl_helhedsoplevelse = []
miks_helhedsoplevelse = []
for i in df['helhedsoplevelse_ems'].values:
    ems_helhedsoplevelse.append(i)
for i in df['helhedsoplevelse_tejl'].values:
    tejl_helhedsoplevelse.append(i)
for i in df['helhedsoplevelse_miks'].values:
    miks_helhedsoplevelse.append(i)
helhedsoplevelse_total = list(map(sum, zip(ems_helhedsoplevelse,tejl_helhedsoplevelse,miks_helhedsoplevelse)))
df['helhedsoplevelse_total'] = helhedsoplevelse_total
    



#CREATE A COLUMN WITH TOTAL OF THE TOTALS!
total_duft = []
total_smag = []
total_helhedsoplevelse = []
for i in df['duft_total'].values:
    total_duft.append(i)
for i in df['smag_total'].values:
    total_smag.append(i)
for i in df['helhedsoplevelse_total'].values:
    total_helhedsoplevelse.append(i)
total_rating = list(map(sum, zip(total_duft,total_smag,total_helhedsoplevelse)))
df['total_rating'] = total_rating




#CREATE A COLUMN WITH TOTAL OF THE TOTALS DIVIDED BY 3.
rating_ = [] 
for i in df['total_rating'].values:
    rating_div = i/3
    rating_.append(rating_div)
rating = ['%.1f' % i for i in rating_]
df['total_rating_div'] = rating





'''
RUN DASH
'''





app = dash.Dash()
server = app.server




'''
LAYOUT
'''





app.layout = html.Div([
    
    html.H1(children = 'Øl julekalender 2022', 
            style = {
        'textAlign': 'center', 
        }),
    
    dcc.Dropdown(
            id='dropdown',
            options=[
                    {'label': 'Smag', 'value': 'Smag'},
                    {'label': 'Duft', 'value': 'Duft'},
                    {'label': 'Helhedsoplevelse', 'value': 'Helhedsoplevelse'},
                    {'label': 'Rating på tværs af kategori', 'value': 'Rating på tværs af kategori'}
            ],
            value = 'Smag',
            style={'width': '50%', 'margins': 'auto'}),
    
    dcc.Graph(id='graf_smag'),



    ])





'''
CALLBACK
'''





@app.callback(
    Output(component_id ='graf_smag', component_property='figure'),
    [Input(component_id='dropdown', component_property='value')])

def update_graph(dropdown_value):
   
    if dropdown_value == 'Smag':
        df.sort_values(by=['smag_total'], inplace=True) 
        fig = go.Figure(
            data=[
                go.Bar(name='Tejlmand', x=df['navn'], y=df['smag_tejl']),
                go.Bar(name='Emma', x=df['navn'], y=df['smag_ems']),
                go.Bar(name='Mikkel', x=df['navn'], y=df['smag_miks'])
                ])
        
    elif dropdown_value == 'Duft':
        df.sort_values(by=['duft_total'], inplace=True) 
        fig = go.Figure(
            data=[
                go.Bar(name='Tejlmand', x=df['navn'], y=df['duft_tejl']),
                go.Bar(name='Emma', x=df['navn'], y=df['duft_ems']),
                go.Bar(name='Mikkel', x=df['navn'], y=df['duft_miks'])
                ])
        
    elif dropdown_value == 'Helhedsoplevelse':
        df.sort_values(by=['helhedsoplevelse_total'], inplace=True) 
        fig = go.Figure(
            data=[
                go.Bar(name='Tejlmand', x=df['navn'], y=df['helhedsoplevelse_tejl']),
                go.Bar(name='Emma', x=df['navn'], y=df['helhedsoplevelse_ems']),
                go.Bar(name='Mikkel', x=df['navn'], y=df['helhedsoplevelse_miks'])
                ])
        
    elif dropdown_value == 'Rating på tværs af kategori':
        df.sort_values(by=['total_rating'], inplace=True) 
        fig = go.Figure(
            data=[
                go.Bar(name='Smag', x=df['navn'], y=df['smag_total']),
                go.Bar(name='Duft', x=df['navn'], y=df['duft_total']),
                go.Bar(name='Helhedsoplevelse', x=df['navn'], y=df['helhedsoplevelse_total'])
                ])
    
    fig.update_layout(barmode='stack')
    fig.layout.template='plotly_white'
    fig.layout.height=400
        
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
