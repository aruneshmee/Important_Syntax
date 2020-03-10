# Making basic graph app in Dash
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {'background':'#111111','text':'#7FDBFF'}

app.layout = html.Div(children=[
    html.H1(children='Hello ol',style ={'textAlign':'center','color':colors['text']}),

    html.Div(children='''
        Dash: A web application framework for Python.
    ''',),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 9], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
############################################ Next Program ################################################  

# Generating Table
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

def generate_table(dataframe, max=10):
    return html.Table([html.Tr([html.Th(col) for col in dataframe.columns])]
    + [html.Tr([html.Td(dataframe.iloc[i][col]) for col in dataframe.columns]) for i in range(min(len(dataframe), max))])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children = [html.H4(children='US....'),generate_table(df)])

if __name__=='__main__':
    app.run_server(debug=True)

############################################ Next Program ################################################      

# Example where a dcc Slider updates a dcc Graph   
import dash  
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input,Output
import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')]
)

def update_figure(select_year):
    filtered_df = df[df.year == select_year]
    traces = []
    for i in filtered_df.continent.unique():
        df_by_continent = filtered_df[filtered_df['continent'] == i]
        traces.append(dict(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            mode='markers',
            opacity=0.7,
            marker={
                'size':15,
                'line':{'width':0.5, 'color':'white'}
            },
            name=i
        ))
    return {
        'data':traces,
        'layout': dict(
            xaxis={'type':'log', 'title':'Gdp per capita', 'range':[2.3,4.8]},
            yaxis={'title':'Life Expectancy', 'range':[20,90]},
            margin={'l':40,'b':40,'t':10,'r':10},
            legend={'x':0, 'y':1},
            hovermode='closest',
            transition={'duration':19000}
        )
    }

if __name__=='__main__':
    app.run_server(debug=True)

############################################ Next Program ################################################   
    
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Input(id='inp-1', type='text'),
        dcc.Input(id='inp-2', type='text'),
        html.Button(id='submit', n_clicks=0, children='submit'),
        html.Div(id='out')
    ]
)

@app.callback(
    Output('out', 'children'),
    [Input('submit', 'n_clicks')],
    [State('inp-1','value'),
    State('inp-2', 'value')]
)

def update_output(n_clicks, inp1, inp2):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(n_clicks, inp1, inp2)

if __name__ == '__main__':
    app.run_server(debug=True)

############################################ Next Program ################################################  

import dash  
import dash_core_components as dcc  
import dash_html_components as html 
from dash.dependencies import Input, Output

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Input(id='input-l', type='text'),
        dcc.Input(id='input-2', type='text'),
        html.Div(id='number-output')
    ]
)

@app.callback(
    Output('number-output', 'children'),
    [Input('input-l','value'), Input('input-2','value')]
)

def update_output(input1, input2):
    return 'input 1 is {} and input 2 is {}'.format(input1, input2)

if __name__=='__main__':
    app.run_server(debug=True)
