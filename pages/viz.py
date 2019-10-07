import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
import data

layout = html.Div([

    dcc.Graph(
        id='graph',
        figure={
            'data': [{
                'type': 'scatter',
                'mode': 'markers',
                'y': data.df['HIT_DISTANCE'].tolist(),
                'x': data.df['LAUNCH_ANGLE'].tolist()
            }],
            'layout': {
                'title': 'Hit Distance vs Launch Angle',
                'yaxis': {
                    'title': 'Hit Distance'
                },
                'xaxis': {
                    'title': 'Launch Angle'
                }
            }
        }
    ),

    html.Div(id='axis-dropdowns', className='row', children=[
        html.Div(className='col', children=[
            html.Div('Y-Axis'),
            dcc.Dropdown(
                id='y-dropdown',
                options=[{'label': i, 'value': i} for i in data.df]
            )
        ]),
        html.Div(className='col', children=[
            html.Div('X-Axis'),
            dcc.Dropdown(
                id='x-dropdown',
                options=[{'label': i, 'value': i} for i in data.df]
            )
        ])
        # html.Div(className='col', children=[
        #     html.Div('Z-Axis'),
        #     dcc.Dropdown(
        #         id='z-dropdown',
        #         options=[{'label': i, 'value': i} for i in data.df]
        #     )
        # ]),
    ]),

    html.Button(
        'Make Graph',
        id='graph-button'
    ),
])

@app.callback(Output('y-dropdown', 'options'),
              [Input('x-dropdown', 'value')])
def update_dropdowns_by_x(x_input):
    ''' Remove the chosen option from the other axis dropdown '''
    new_options = [{'label': i, 'value': i} for i in data.df]
    chosen = {'label': x_input, 'value': x_input}
    if chosen in new_options:
        new_options.remove({'label': x_input, 'value': x_input})
    return new_options

@app.callback(Output('x-dropdown', 'options'),
              [Input('y-dropdown', 'value')])
def update_dropdowns_by_y(y_input):
    ''' Remove the chosen option from the other axis dropdown '''
    new_options = [{'label': i, 'value': i} for i in data.df]
    chosen = {'label': y_input, 'value': y_input}
    if chosen in new_options:
        new_options.remove({'label': y_input, 'value': y_input})
    return new_options

@app.callback(Output('graph', 'figure'),
              [Input('graph-button', 'n_clicks')],
              [State('y-dropdown', 'value'),
               State('x-dropdown', 'value')])
def make_graph(n_clicks, y_value, x_value):
    if n_clicks == 0:
        return {
            'data': [{
                'type': 'scatter',
                'mode': 'markers',
                'y': data.df['HIT_DISTANCE'].tolist(),
                'x': data.df['LAUNCH_ANGLE'].tolist()
            }],
            'layout': {
                'title': 'Hit Distance vs Launch Angle',
                'yaxis': {
                    'title': 'Hit Distance'
                },
                'xaxis': {
                    'title': 'Launch Angle'
                }
            }
        }

    return {
        'data': [{
            'type': 'scatter',
            'mode': 'markers',
            'y': data.get_column_data(y_value),
            'x': data.get_column_data(x_value)
        }],
        'layout': {
            'title': y_value + ' vs ' + x_value,
            'yaxis': {
                'title': y_value
            },
            'xaxis': {
                'title': x_value
            }
        }
    }
