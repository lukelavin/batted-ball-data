import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output

from app import app
from data import df

layout = dash_table.DataTable(
                id='table',
                columns = [
                    {'id': i, 'name': i} for i in df.columns
                ],
                data = df.to_dict('records'),
                sort_action="native",
                sort_mode="single",
                loading_state={'is_loading': True}
            )
