import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H5("Components", className="text-left")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.Img(src="/assets/SCP.jpg", width="50%")),
            dbc.Col(html.Img(src="/assets/DEA.jpg", width="50%"))
        ]),
        dbc.Row([
            dbc.Col(html.H6("Super-coiled Polymer Actuator", className="text-left")
                    , className="mb-5 mt-5", ),
            dbc.Col(html.H6("Dielectric Elastomer Actuator", className="text-left")
                    , className="mb-5 mt-5"),
        ]),
        dbc.Row([
            dbc.Col(html.A(children='Super-coiled polymer actuators (SCPs) are manufactured by '
                                    'twisting nylon filaments until a tight helical coil is formed. These coils '
                                    'can be actuated by electric power and should be under a load to keep the muscle '
                                    'extended.')
                    , className="mb-5"),
            dbc.Col(html.A(children='Dialectric elastomer actuators (DEAs) convert electrical energy directly '
                                    'into a mechanical output. DEAs can be made completely soft and demonstrate energy '
                                    'and power densities comparable to natural muscles.')
                    , className="mb-5")
        ]),
        dbc.Row([
            dbc.Col(html.Img(src="/assets/SMA.jpg", width="50%")),
            dbc.Col(html.Img(src="/assets/PZ.jpg", width="50%"))
        ]),
        dbc.Row([
            dbc.Col(html.H6("Shape Memory Alloy Actuator", className="text-left")
                    , className="mb-5 mt-5", ),
            dbc.Col(html.H6("Piezoelectric Actuator", className="text-left")
                    , className="mb-5 mt-5"),
        ]),
        dbc.Row([
            dbc.Col(html.A(children='Shape memory alloys (SMAs) are metallic materials that can revert to their '
                                    'original shape at certain temperatures. One benefit of SMAs is that they have '
                                    'high power-to-weight ratios.')
                    , className="mb-5"),
            dbc.Col(html.A(children='Similar to DEAs, piezoelectric actuators (PZTs) use electrical energy to exert '
                                    'a mechanical force, which is especially useful for small displacements that '
                                    'require extremely precise movements.')
                    , className="mb-5")
        ])
    ])
])

# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)