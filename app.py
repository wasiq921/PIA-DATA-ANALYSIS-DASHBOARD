from flask import Flask, render_template
#import dash
from dash import Dash
from dash import dcc
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input, Output
#from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
import plotly.graph_objs as go
#import dash_html_components as html
from dash import html
#import numpy as np
from dash import callback_context
import pandas as pd
import dash_bootstrap_components as dbc

server = Flask(__name__)


dashapp1 = Dash(__name__, external_stylesheets=['dbc.themes.BOOTSTRAP'], title = 'Maintenance Dashboard', server = server, url_base_pathname='/maintenancedashboard/')
dashapp2 = Dash(__name__, external_stylesheets=['dbc.themes.BOOTSTRAP'], title = 'Repair Dashboard', server = server, url_base_pathname='/repairdashboard/')
dashapp3 = Dash(__name__, external_stylesheets=['dbc.themes.BOOTSTRAP'], title = 'Operations Dashboard', server = server, url_base_pathname='/operationsdashboard/')

@server.route('/')
def home():  # put application's code here
    return render_template('select.html')


@server.route('/maintenance_login')
def maintenance_login():  # put application's code here
    return render_template('Maintainance_login.html')


@server.route('/repair_login')
def repair_login():  # put application's code here
    return render_template('Repair_login.html')



@server.route('/operations_login')
def operations_login():  # put application's code here
    return render_template('Operations_login.html')


@server.route('/maintenance')
def maintenance():  # put application's code here
    return render_template('Maintainance.html')


@server.route('/repair')
def repair():  # put application's code here
    return render_template('repair.html')


@server.route('/operations')
def operations():  # put application's code here
    return render_template('Operations.html')



app = DispatcherMiddleware(server, {
    '/dash1': dashapp1.server,
    '/dash2': dashapp2.server,
    '/dash3': dashapp3.server
})

@server.route('/maintenancedashboard')
def render_dashboard():
    return flask.redirect('/dash1')


@server.route('/repairdashboard')
def render_reports():
    return flask.redirect('/dash2')


@server.route('/operationsdashboard')
def render_operationsreports():
    return flask.redirect('/dash3')




df = pd.read_csv('flight_summary_report_updated.csv')

#card1 = dbc.Card([
#    dbc.CardBody([
#        html.H4("Total Fleet Capacity", className="card-title",id="card_num1"),
#        html.P(f"{df['Capacity'].sum()} ", className="card-text",id="card_text1")
#    ])
#],
#    style={'display': 'inline-block',
#           'width': '33.3%',
#           'text-align': 'center',
#           'background-color': 'rgba(37, 150, 190)'},
#    outline=True)


all = df['Route'].unique()

dashapp1.layout = html.Div(
      style={
      #'background-image': "url('dashboard-project/image2.png')",
             'background-image' : "url('assets/image2.png')",
               'background-repeat': 'no-repeat',
          'background-position': 'left top',
           'background-size': '200px 100px',
           'margin-left' : '50px',
           'margin-top' : '20px',
    },
    children =[
    
     dbc.Row([
        dbc.Col([
            html.H1('MAINTENANCE DASHBOARD', style={'textAlign':'center', 'color' : 'darkgreen', 'font-weight' : 'bold', 'font-size': '300%', 'margin-left' :'50px' ,'font-family' : 'helvetica'}),
        ])
    ]),
    
    
        
        html.Br(),
    html.Br(),
        html.Br(),
    html.Br(),
    
    dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                id='my_checklist',                      # used to identify component in callback
                
                  #  [{'label':x, 'value':x} for x in all] + [{'label': 'Select all', 'value': 'all_values'}],
                       options=[{'label':x, 'value':x} for x in all] + [{'label': 'Select all', 'value': 'all_values'}], 
                    value=['PEWKHI','LHEDXB', 'KHIIST'], 
                    placeholder = 'Select Route',
                
                
                multi = True
                
               # style={'width':113, 'overflowY': 'scroll', 'height': 150, 'dsiplay': 'inline:block', 'margin-right' : 50}
                
                )],style = { 'width': '25%', 'display': 'inline-block', 'margin-left' : '100px'}),
    
 #       dbc.Col([
 #           dcc.Dropdown(
 #               id='date',                      # used to identify component in callback
 #               options=[
 #                        {'label': x, 'value': x, 'disabled':False}
 #                        for x in df['Sch Dep Date'].unique()
 #               ],
 #               value= [],
 #               multi = True,
 #               placeholder = 'Select Date'
 #               
                
               # style={'width':113, 'overflowY': 'scroll', 'height': 150, 'display': 'block'}
                
  #              ),#values chosen by default
            
   #     ], style = { 'width': '25%', 'display': 'inline-block', 'margin-left' : '100px', })
]),
    
    html.Div([
        html.Br(),
        html.Br(),
       # card1 
    #color="warning" , style = { 'width': '15%','margin-left' : '550px', 'color': 'white', 'background-color' : 'green', 'textAlign' : 'center', 'height' : '25%'},
]),

    html.Br(),
    html.Br(),
    
    html.Div([
        dcc.Graph(
        id  = 'sample_graph',
            
        
        #figure = px.histogram(df, x="Ac name", color="Oper type")
        )
    ],
        style = { 'width': '50%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(
        id  = 'sample_graph1',
        #figure = px.histogram(df, x="Oper type", color="Ac type")
        #figure = px.histogram(df, x="Oper type", color="Ac type")
        )
    ],
        style = { 'width': '50%', 'display': 'inline-block'}),
    
    
    html.Div([
        html.Br(),
        html.Br(),
        dcc.Graph(
        id = 'pie-chart',
       # figure  = px.pie(df, values="Number of fleets", names="Oper type"),
            
    
        )
    ],
    style = { 'width': '50%', 'display': 'inline-block',  'position' : 'center'}),
        
        html.Div([
        html.Br(),
        html.Br(),
        dcc.Graph(
        id = 'pie-chart1',
       # figure  = px.pie(df, values="Number of fleets", names="Oper type"),
            
    
        )
    ],
    style = { 'width': '50%', 'display': 'inline-block',  'position' : 'center'})
        
        
    
],
  
)
@dashapp1.callback(
        Output('card_num1','children'),
        Output('card_text1','children'),
  
        [Input('my_checklist', 'value')],
)
        

def update_card(Route_dropdown_name):
        dff = df[(df.Route == Route_dropdown_name)]
        dff2 = pops[pops['Route'] == Route_dropdown_name]

        card1 = dbc.Card([
                dbc.CardBody([
                    html.H4("Total Fleet Capacity", className="card-title",id="card_num1"),
                    html.P("{Route_dropdown_name}", className="card-text",id="card_text1")
                     ])
             ],
             style={'display': 'inline-block',
             'width': '33.3%',
             'text-align': 'center',
             'background-color': 'rgba(37, 150, 190)'},
             outline=True)
       
        
        
        
        
            
            
        
                 
  #  fig.add_trace(px.histogram(df, x="Oper type", color="Ac type"))
        

@dashapp1.callback(
        Output('sample_graph1', 'figure'),
  
        [Input('my_checklist', 'value')],
)
        

def update_figure(Route_dropdown_name):
        if Route_dropdown_name  == ['all']:
            dff = df
        else:
            dff = df[df['Route'].isin(Route_dropdown_name)]
            fig = px.histogram(dff, x="Oper type", color="Ac type", title = 'Operations Type and Account Type')
            fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                 
            })
            fig.update_layout(showlegend=True)
            fig.update_layout(legend = dict(bgcolor = 'white'))
            
        
                 
  #  fig.add_trace(px.histogram(df, x="Oper type", color="Ac type"))
        return fig


#@app.callback(
#        Output('sample_graph1', 'figure'),
#        [Input('date', 'value')]
        
#)
        

#def update_figure(Route_dropdown_name):
#        if Route_dropdown_name == ['all']:
 #           dff = df
  #      else:
   #         dff = df[df['Sch Dep Date'].isin(Rouute_dropdown_name)]
     #      fig = go.Figure()
       #     fig.add_trace(go.Histogram(histfunc="count",  x=dff['Oper type'])
         #        )
  #  fig.add_trace(px.histogram(df, x="Oper type", color="Ac type"))
        #return fig

@dashapp1.callback(
        Output('sample_graph', 'figure'),
        [Input('my_checklist', 'value')],
)
        

def update_figure(Route_dropdown_name):
        if Route_dropdown_name == ['all']:
            dff = df
        else:
            dff = df[df['Route'].isin(Route_dropdown_name)] 
            fig = px.histogram(dff, x="Ac name", color="Oper type", title = 'Account Name and Operations Type')
            fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                 
            })
            fig.update_layout(showlegend=True)
            fig.update_layout(legend = dict(bgcolor = 'white'))
                 
  #  fig.add_trace(px.histogram(df, x="Oper type", color="Ac type"))
        return fig


@dashapp1.callback(
        Output('pie-chart', 'figure'),
        [Input('my_checklist', 'value')],
)
        

def update_figure(Route_dropdown_name):
        if Route_dropdown_name == ['all']:
            dff = df
        else:
            dff = df[df['Route'].isin(Route_dropdown_name)] 
            fig = px.pie(dff, values="Number of fleets", names="Oper type", title = 'Total Number of Fleets and Operations Type')
            fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                 
            })
            fig.update_layout(showlegend=True)
            fig.update_layout(legend = dict(bgcolor = 'white'))
        return fig
                 
  #  fig.add_trace(px.histogram(df, x="Oper type", color="Ac type"))

@dashapp1.callback(
        Output('pie-chart1', 'figure'),
        [Input('my_checklist', 'value')],
)


def update_figure(Route_dropdown_name):
        if Route_dropdown_name == ['all']:
            dff = df
        else:
            dff = df[df['Route'].isin(Route_dropdown_name)] 
            fig = px.pie(dff, values="Number of fleets", names="Source", title = 'Total Number of Fleets and Source')
            fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                 
            })
            fig.update_layout(showlegend=True)
            fig.update_layout(legend = dict(bgcolor = 'white'))
        return fig
        




dashapp2.layout = html.Div(
    style={#'background-image': "url('/assets/image2.png')"
            'background-image': "url('assets/image2.png')",
               'background-repeat': 'no-repeat',
          'background-position': 'left top',
           'background-size': '200px 100px',
           'margin-left' : '50px',
           'margin-top' : '20px',
    }
   , children = [
       dbc.Row([
        dbc.Col([
            html.H1('REPAIRS DASHBOARD', style={'textAlign':'center', 'color' : 'darkgreen', 'font-weight' : 'bold', 'font-size': '300%', 'margin-left' :'50px' ,'font-family' : 'helvetica'}),
        ])
    ]),
    
    html.Br(),
    html.Br(),
       html.Br(),
    html.Br(),
    
    html.Div([
            dcc.Dropdown(
                id='account_type',                      # used to identify component in callback
                options=[
                  #  [{'label':x, 'value':x} for x in all] + [{'label': 'Select all', 'value': 'all_values'}],
                        {'label': x, 'value': x, 'disabled':False}
                       for x in (df['Source'].unique()) ],
                    value=['PAX', 'BSP'],
                
                placeholder = 'Select Source',
                multi = True
                
               # style={'width':113, 'overflowY': 'scroll', 'height': 150, 'dsiplay': 'inline:block', 'margin-right' : 50}
                
                )],style = { 'width': '25%', 'display': 'inline-block', 'margin-left' : '100px'}),
    
        
    
    html.Br(),
    html.Br(),
    
    html.Div([
        dcc.Graph(
        id  = 'date_ac_name',
        #figure = px.histogram(df, x="Ac name", color="Oper type")
        )
    ],
        style = { 'width': '50%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(
        id  = 'date_ac_type',
        #figure = px.histogram(df, x="OPS_CODE", color="TYPE_CODE")
        )
    ],
        style = { 'width': '50%', 'display': 'inline-block'}),
    
    
    html.Div([
        html.Br(),
    html.Br(),
        dcc.Graph(
        id = 'flight_no_oper_type',
         #fig = px.pie(dff, values="FLT_NO", names="AC_REG")
            
        
       # figure =px.pie(df, values="Number of fleets", names="Oper type")
        )
    ]
        , style = { 'width': '50%', 'display': 'inline-block'}
    ),
   
    
        html.Div([
            html.Br(),
    html.Br(),
        dcc.Graph(
        id = 'flight_no_route',
        
       # figure =px.pie(df, values="Number of fleets", names="Oper type")
        )
    ],
         style = { 'width': '50%', 'display': 'inline-block'}
        )
    
])

@dashapp2.callback(
        Output('date_ac_name', 'figure'),
        [Input('account_type', 'value'),]
        
)
        

def update_figure(account_dropdown_name):
        if account_dropdown_name  == ['all']:
            dff = df
        else:
            dff = df[df['Source'].isin(account_dropdown_name)]
        fig = px.histogram(dff, x="Ac name", color="Sch Dep Date", title = 'Account Name and Departure Date', labels={
                     "Ac name": "Account Name",
                 })
        fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                 
            })
        fig.update_layout(showlegend=True)
        fig.update_layout(legend = dict(bgcolor = 'white'))
            
        
                 
  #  fig.add_trace(px.histogram(df, x="Oper type", color="Ac type"))
        return fig

#@app.callback(
#        Output('sample_graph1', 'figure'),
#        [Input('date', 'value')]
        
#)
        

#def update_figure(Route_dropdown_name):
#        if Route_dropdown_name == ['all']:
 #           dff = df
  #      else:
   #         dff = df[df['Sch Dep Date'].isin(Rouute_dropdown_name)]
     #      fig = go.Figure()
       #     fig.add_trace(go.Histogram(histfunc="count",  x=dff['Oper type'])
         #        )
  #  fig.add_trace(px.histogram(df, x="Oper type", color="Ac type"))
        #return fig


    
    
@dashapp2.callback(
        Output('date_ac_type', 'figure'),
        [Input('account_type', 'value'),]
        
)
        

def update_figure(account_dropdown_name):
        if account_dropdown_name  == ['all']:
            dff = df
        else:
            dff = df[df['Source'].isin(account_dropdown_name)]
        fig = px.pie(dff, values="Capacity", names="Ac type", title = 'Total Capacity and Account Type')
        fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                 
            })
        fig.update_layout(showlegend=True)
        fig.update_layout(legend = dict(bgcolor = 'white'))
        
                 
  #  fig.add_trace(px.histogram(df, x="Oper type", color="Ac type"))
        return fig


@dashapp2.callback(
        Output('flight_no_oper_type', 'figure'),
        [Input('account_type', 'value'),],
)
        

def update_figure(account_dropdown_name):
        if account_dropdown_name == ['all']:
            dff = df
        else:
            dff = df[df['Source'].isin(account_dropdown_name)] 
            fig = px.pie(dff, values="Flt no", names="Oper type", title = 'Operations Type and Flight Number')
            fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                 
            })
            fig.update_layout(showlegend=True)
            fig.update_layout(legend = dict(bgcolor = 'white'))
        return fig
    
    
@dashapp2.callback(
        Output('flight_no_route', 'figure'),
        [Input('account_type', 'value'),],
)
        

def update_figure(account_dropdown_name):
        if account_dropdown_name == ['all']:
            dff = df
        else:
            dff = df[df['Source'].isin(account_dropdown_name)] 
            fig = fig = px.histogram(dff, color="Reporting group name", x='Sch Dep Date', title = 'Departure Date and Reporting Group Name') #, color="continent",line_group="country")
            fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                 
            })
            fig.update_layout(showlegend=True)
            fig.update_layout(legend = dict(bgcolor = 'white'))
        return fig
                 
  #  fig.add_trace(px.histogram(df, x="Oper type", color="Ac type"))

df1 = pd.read_csv('old_data.csv')
df1.dropna(inplace = True)
df1['OPS_CODE'].dropna(inplace = True)




dashapp3.layout = html.Div(
    style={'background-image': "url('assets/image2.png')",
               'background-repeat': 'no-repeat',
          'background-position': 'left top',
           'background-size': '200px 100px',
           'margin-left' : '50px',
           'margin-top' : '20px',
    }
   , children = [
       dbc.Row([
        dbc.Col([
            html.H1('OPERATIONS DASHBOARD', style={'textAlign':'center', 'color' : 'darkgreen', 'font-weight' : 'bold', 'font-size': '300%', 'margin-left' :'50px' ,'font-family' : 'helvetica'}),
        ])
    ]),
    
    html.Br(),
    html.Br(),
       html.Br(),
    html.Br(),
    
    html.Div([
            dcc.Dropdown(
                id='registration',                      # used to identify component in callback
                options=[
                  #  [{'label':x, 'value':x} for x in all] + [{'label': 'Select all', 'value': 'all_values'}],
                        {'label': x, 'value': x, 'disabled':False}
                       for x in (df1['AC_REG'].unique()) ],
                    value=['ALW', 'BAL', 'BCD', 'BCC'],
                
                placeholder = 'Select Account Registration',
                multi = True
                
               # style={'width':113, 'overflowY': 'scroll', 'height': 150, 'dsiplay': 'inline:block', 'margin-right' : 50}
                
                )],style = { 'width': '25%', 'display': 'inline-block', 'margin-left' : '100px'}),
    
        
    
    html.Br(),
    html.Br(),
    
    html.Div([
        dcc.Graph(
        id  = 'stn_from_stn_to',
        #figure = px.histogram(df, x="Ac name", color="Oper type")
        )
    ],
        style = { 'width': '50%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(
        id  = 'ops_code',
        figure = px.histogram(df1, x="OPS_CODE", color="TYPE_CODE")
        )
    ],
        style = { 'width': '50%', 'display': 'inline-block'}),
    
    
    html.Div([
        html.Br(),
    html.Br(),
        dcc.Graph(
        id = 'pie-chart_num_of _plane',
         #fig = px.pie(dff, values="FLT_NO", names="AC_REG")
            
        
       # figure =px.pie(df, values="Number of fleets", names="Oper type")
        )
    ]
        , style = { 'width': '50%', 'display': 'inline-block'}
    ),
   
    
        html.Div([
            html.Br(),
    html.Br(),
        dcc.Graph(
        id = 'pie-chart_ops_code',
        
       # figure =px.pie(df, values="Number of fleets", names="Oper type")
        )
    ],
         style = { 'width': '50%', 'display': 'inline-block'}
        )
    
])

@dashapp3.callback(
        Output('stn_from_stn_to', 'figure'),
        [Input('registration', 'value'),]
        
)
        

def update_figure(registration_dropdown_name):
        if registration_dropdown_name  == ['all']:
            dff1 = df1
        else:
            dff1 = df1[df1['AC_REG'].isin(registration_dropdown_name)]
        fig = px.histogram(dff1, x="STN_FROM", color="STN_TO", title = 'Departure City and Arrival City', labels={
                     "STN_FROM": "Depart From",
                 })
        fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                 
            })
        fig.update_layout(showlegend=True)
        fig.update_layout(legend = dict(bgcolor = 'white'))
            
        
                 
  #  fig.add_trace(px.histogram(df, x="Oper type", color="Ac type"))
        return fig

#@app.callback(
#        Output('sample_graph1', 'figure'),
#        [Input('date', 'value')]
        
#)
        

#def update_figure(Route_dropdown_name):
#        if Route_dropdown_name == ['all']:
 #           dff = df
  #      else:
   #         dff = df[df['Sch Dep Date'].isin(Rouute_dropdown_name)]
     #      fig = go.Figure()
       #     fig.add_trace(go.Histogram(histfunc="count",  x=dff['Oper type'])
         #        )
  #  fig.add_trace(px.histogram(df, x="Oper type", color="Ac type"))
        #return fig


    
    
@dashapp3.callback(
        Output('ops_code', 'figure'),
        [Input('registration', 'value'),]
        
)
        

def update_figure(registration_dropdown_name):
        if registration_dropdown_name  == ['all']:
            dff1 = df1
        else:
            dff1 = df1[df1['AC_REG'].isin(registration_dropdown_name)]
        fig = px.histogram(dff1, x="TYPE_CODE", color="OPS_CODE", title = 'Operations Code and Type Code')
        fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                 
            })
        fig.update_layout(showlegend=True)
        fig.update_layout(legend = dict(bgcolor = 'white'))
        
                 
  #  fig.add_trace(px.histogram(df, x="Oper type", color="Ac type"))
        return fig


@dashapp3.callback(
        Output('pie-chart_num_of _plane', 'figure'),
        [Input('registration', 'value'),],
)
        

def update_figure(registration_dropdown_name):
        if registration_dropdown_name == ['all']:
            dff1 = df1
        else:
            dff1 = df1[df1['AC_REG'].isin(registration_dropdown_name)] 
            fig = px.pie(dff1, values="FLT_NO", names="AC_REG", title = 'Account Registration and Total Flight Numbers')
            fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                 
            })
            fig.update_layout(showlegend=True)
            fig.update_layout(legend = dict(bgcolor = 'white'))
        return fig
    
    
@dashapp3.callback(
        Output('pie-chart_ops_code', 'figure'),
        [Input('registration', 'value'),],
)
        

def update_figure(registration_dropdown_name):
        if registration_dropdown_name == ['all']:
            dff1 = df1
        else:
            dff1 = df1[df1['AC_REG'].isin(registration_dropdown_name)] 
            fig = px.pie(dff1, values="Day", names="TYPE_CODE", title = 'Total Flight Hours and Type Code')
            fig.update_layout({
                'plot_bgcolor': 'rgba(0,0,0,0)',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                 
            })
            fig.update_layout(showlegend=True)
            fig.update_layout(legend = dict(bgcolor = 'white'))
        return fig
                 
  #  fig.add_trace(px.histogram(df, x="Oper type", color="Ac type"))


#run_simple(8080, app, use_reloader=True, use_debugger=True)

if __name__ == '__main__':
    server.run()
