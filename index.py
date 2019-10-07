import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import os

from app import app
from pages import viz, home, inspect_data


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    html.Div(id='header', className='row', children=[
        html.H1(
            id='title',
            className='col',
            style={
                'padding-left': '25px',
                'padding-right': '25px',
            },
            children=html.Img(className='vertical-align', src=app.get_asset_url('logo.svg'), style={
                    'width': '5rem',
                    'height': '5rem'
            })
        ),

        html.Div(id='nav', className='col right', children=[
            dcc.Link('Home', href='/', style={'padding-left': '25px', 'padding-right': '25px', 'color': '#101010'}),
            dcc.Link('Visualize', href='/viz', style={'padding-left': '25px', 'padding-right': '25px', 'color': '#101010'}),
            dcc.Link('Inspect Data', href='/data', style={'padding-left': '25px', 'padding-right': '25px', 'color': '#101010'}),
        ])
    ]),

    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/viz':
        return viz.layout
    elif pathname == '/':
        return home.layout
    elif pathname == '/data':
        return inspect_data.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server()
