import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H5("What is the robot muscles toolkit?", className="text-left")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='The Robot Muscles Toolkit is a collection of shared resources to support the '
                                     'design, facbrication, modeling, characterization, and control of robot muscle devices. '
                                     'The Toolkit was developed as part of educational research being undertaken by the '
                                     'collaboration of Professor Yip from University of California, San Diego and Professor '
                                     'Wood from Harvard University.') 
                    , className="mb-4")
            ])
    ])
])

# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)