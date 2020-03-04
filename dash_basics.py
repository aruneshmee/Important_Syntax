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
