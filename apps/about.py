import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H5("About", className="text-left")
                    , className="mb-5 mt-5")
        ]), 
        dbc.Row([
            dbc.Col(html.A(children='The objective of the Robot Muscle Toolkit is to develop a foundational approach towards '
                                     'muscle-powered machines that move using biomimetic muscle actuators. Biomimetic muscle '
                                     'actuators, or robot muscles are actuators that closely mimic the propoerties of '
                                     'biological muscles in nature. These robot muscle technologies have covered a varied range '
                                     'of configurations, including notable examples from shape-memory alloys (SMAs) and dielectric '
                                     'elastomers (DEAs), to super-coiled polymers (SCPs) and piezoelectric actuators (PZTs). '
                                     'They offer unique properties of controlled compliances, large bandwidth ranges, high '
                                     'power-to-weight ratios and compact muscle-like form factors, over a range of scales from '
                                     'micro- to macroscopic actuators. When compared to traditional actuators such as motor '
                                     'or hydraulics these properties are valuable in realizing compliant, compact, and safe '
                                     'robot designs and operations.')
                    , className="mb-5")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='Despite the decades of materials research in discovering new muscles and improving '
                                    'existing muscles, their transition into more widescpread use in robot systems and '
                                    'machines to date has been limited. We argue that this is because actuators, when '
                                    'considered as dissimilar and distinct technologies, have significant challenges '
                                    'for robot designers to overcome: 1) it is unclear how to select or even compare '
                                    'muscle actuators for use in an application, 2) they exhibit significant nonlinear '
                                    'behaviors that require non-trivial modeling, control, and design, resting the burden '
                                    'of use on the robot designer, and 3) few resources are available for academic '
                                    'researchers to manufacture repeatable and stable actuators and compare performance '
                                    'with state-of-art developments.')
                    , className="mb-5")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='Robot Muscle Toolkit therefore provides a unifying modeling, control, and design '
                                    'strategy for robot muscles that lowers the barrier to muscle-powered robotics '
                                    'research by focusing on accessible muscle-powered robot design and benchmarking.')
                    , className="mb-5")
        ])
    ])

])

# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)