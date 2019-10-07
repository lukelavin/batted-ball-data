import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
import data

layout = html.Div([
    html.Div(
        children=[

            html.H4('Intro'),

            html.Div('''
            I created a tool that can be used to analyze ''' +
            str(len(data.df)) +
            '''
            batted balls, from ''' +
            str(len(data.df['PITCHER'].append(data.df['BATTER']).unique())) +
            '''
            players, through ''' +
            str(len(data.get_column_data_unique('GAME_DATE'))) +
            '''
            days worth of games. It uses Dash by plotly, which is a framework for
            making data analytics dashboards based on Flask and React. It can
            dynamically create graphics for user-chosen variables, and it can display
            data in a dynamic table that can be sorted and paged through.
            '''),


            html.H4('What I Am Happy With'),

            html.Div('''
            The one thing I'm most happy with about this project is what I've learned.
            Overall, this has been a really fun process of learning Dash, a framework
            I have had no previous experience with. It seems easy to use, yet very
            powerful. Also, most of my previous experience has been on the backend
            of projects, and simply getting more experience on the frontend side
            of things is valuable to me.
            '''),
            html.Br(),
            html.Div('''
            For what this tool can do, it does it welll. It looks nice and is very functional.
            Dash provides a lot of functionality and polish through its own modules, which
            made it very easy to get something running quickly (even including
            the time it took me to learn Dash).
            '''),
            html.Br(),


            html.H4('What I Would Like To Improve'),

            html.Div('''
            If this were a real, long-term project, I would have worked harder
            to get to know the users very well. With a tool like this, the focus
            should be on making the target audience's analysis easier and more
            insightful, so communicating with my audience and getting to know
            their workflow better would have been helpful.
            '''),
            html.Br(),
            html.Div('''
            Apart from that, being constrained to 5 hours and being limited by my
            other committments, I just couldn't implement everything I had envisioned.
            Obviously, I would love to implement more features. More filtering--being
            able to look at data only against certain teams, on a specific day of the week,
            against left-handed pitchers only, within a certain date range etc. More graph
            types--the scatter plot is a good all-arounder, but for some data it's not the best choice,
            and for other data it makes no sense whatsoever. 3-dimensional analysis--
            using two independent variables and viewing their impact on some dependent
            variable (for example: a heat map showing how number of home runs relates
            to both exit speed and launch angle). Other improvements could include
            viewing averages for specific batters/pitchers, graphing measures of
            central tendency rather than all ~8000 data points, an upload functionality
            to import new data, etc. There's still lots that can be done feature-wise.
            '''),
            html.Br(),
            html.Div('''
            There are also a few places that could use a little polishing.

            For example, the table loads a little bit slow, at least slow enough where I
            should add a loading symbol while it loads. I believe this should be
            possible in Dash, but I never got the time to look into it.

            Hovering over data points on graphs should provide more useful info
            than just the values already shown on the graph. Instead, it could
            show the pitcher, batter, date, and or video link.
            '''),

            html.H4('Conclusion'),

            dcc.Markdown('''
            To be honest, **I felt like I was just getting started**.
            There is so much more that I can do with this tool now that I am more
            comfortable with Dash, and now that the structure of the app is set up.
            However, the deadline has arrived, and anyways, spending more than
            the estimated 5 hours on this assignment would likely misrepresent
            my skills.
            '''),

            dcc.Markdown('''
            This has been a ton of fun, and I will likely still work on this
            even after I submit it. I hope that even if my product isn't particularly
            impressive yet, you can see the thought I put into it and my passion for it.
            '''),

            html.H4('Some images created using this tool:'),
            html.Img(src=app.get_asset_url('dist_vs_angle.png')),
            html.Img(src=app.get_asset_url('outcome_vs_hangtime.png')),
            html.Img(src=app.get_asset_url('dist_vs_speed.png')),
        ],
        style={
            'padding-left': '15rem',
            'padding-right': '15rem'
        })
])
