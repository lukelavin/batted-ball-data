import dash

external_stylesheets = ['https://unpkg.com/wingcss@1.0.0-beta/dist/wing.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Batted Ball Data Tool'
app.config.suppress_callback_exceptions=True
