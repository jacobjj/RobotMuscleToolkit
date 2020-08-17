import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H5("Our Research", className="text-left")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='Below is a guide to our research on the classification of different actuators based '
                                    'on their class. We focused on the following classes of actuators: SMA, PZT, DEA, '
                                    'IPMC, SCP, SFA, TSA, and EAP.')
                    , className="mb-5")
        ])
    ])
])

# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)