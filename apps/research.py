import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc

import pandas as pd

from app import app

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#read csv
df = pd.read_csv('data.csv')

# remove SMP actuator types 
df = df[df['Actuator Type'] != 'SMP']

#define available columns for graphing
available_indicators = df.columns[2:7]

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H5("Our Research", className="text-left")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='The following graph displays the distribution of actuator types based on their '
                                    'class, with the classes of actuators being PZT, DEA, IPMC, SMA, SFA, TSA, SCP, and '
                                    'EAP. All data shown has been collected from published research papers.')
                    , className="mb-5")
        ]),
        #define dropdown for x values
        dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Strain (%)',
                style={'width': '48%', 'display': 'inline-block'}
        ),

        #define dropdown for y values
        dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Stress (MPa)',
                style={'width': '48%', 'float': 'right', 'display': 'inline-block'}
        ),
        #set up graph
        dcc.Graph(id='indicator-graphic'),
        dbc.Row([
            dbc.Col(html.P(children='')
                , className="mb-5")
        ]),
        dbc.Row([
            dbc.Col(html.P(children='Below is a multi-class contour representation of the different actuator classes.')
                , className="mb-5")
        ]),
        dcc.Dropdown(
            id='xaxis-dd',
            options=[
                {'label': 'Bandwidth (Hz)', 'value': 'Bandwidth'},
                {'label': 'Strain (%)', 'value': 'Strain'},
                {'label': 'Stress (MPa)', 'value': 'Stress'},
                {'label': 'Efficiency (%)', 'value': 'Efficiency'},
                {'label': 'Power Density (W/g)', 'value': 'Power Density'}
            ],
            value='Strain',
            style={'width': '48%', 'display': 'inline-block'}
        ),
        dcc.Dropdown(
            id='yaxis-dd',
            options=[
                {'label': 'Bandwidth (Hz)', 'value': 'Bandwidth'},
                {'label': 'Strain (%)', 'value': 'Strain'},
                {'label': 'Stress (MPa)', 'value': 'Stress'},
                {'label': 'Efficiency (%)', 'value': 'Efficiency'},
                {'label': 'Power Density (W/g)', 'value': 'Power Density'}
            ],
            value='Stress',
            style={'width': '48%', 'float': 'center', 'display': 'inline-block'}
        ),
        html.Img(
                id='dropdown-output')
    ])
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value')])

#updates x and y values based on dropdown and indicates each dot by actuator type
def update_graph(xaxis_column_name, yaxis_column_name):
    traces = []
    for i in df["Actuator Type"].unique():
        df_by_actuator = df[df['Actuator Type'] == i]
        traces.append(dict(
            x=df_by_actuator[xaxis_column_name],
            y=df_by_actuator[yaxis_column_name],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.7, 'color': 'white'}
            },
            name=i
        ))


    return {
        'data': traces,
        'layout': dict(
            xaxis={
                'title': xaxis_column_name
            },
            yaxis={
                'title': yaxis_column_name
            },
            margin={'l': 80, 'b': 30, 't': 10, 'r': 0},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }

@app.callback(
    Output('dropdown-output', 'src'),
    [Input('xaxis-dd', 'value'),
    Input('yaxis-dd', 'value')])

def update_output(xaxis_value, yaxis_value):
    if xaxis_value == 'Strain' and yaxis_value == 'Stress':
        src = "/assets/contour/strain vs stress.png"
    elif xaxis_value == 'Bandwidth' and yaxis_value == 'Bandwidth':
        src = "/assets/contour/bandwidth vs bandwidth.png"
    elif xaxis_value == 'Bandwidth' and yaxis_value == 'Strain':
        src = "/assets/contour/bandwidth vs strain.png"
    elif xaxis_value == 'Bandwidth' and yaxis_value == 'Stress':
        src = "/assets/contour/bandwidth vs stress.png"
    elif xaxis_value == 'Bandwidth' and yaxis_value == 'Efficiency':
        src = "/assets/contour/bandwidth vs efficiency.png"
    elif xaxis_value == 'Bandwidth' and yaxis_value == 'Power Density':
        src = "/assets/contour/bandwidth vs power density.png"
    elif xaxis_value == 'Strain' and yaxis_value == 'Bandwidth':
        src = "/assets/contour/strain vs bandwidth.png"
    elif xaxis_value == 'Strain' and yaxis_value == 'Efficiency':
        src = "/assets/contour/strain vs efficiency.png"
    elif xaxis_value == 'Strain' and yaxis_value == 'Power Density':
        src = "/assets/contour/strain vs power density.png"
    elif xaxis_value == 'Strain' and yaxis_value == 'Strain':
        src = "/assets/contour/strain vs strain.png"
    elif xaxis_value == 'Stress' and yaxis_value == 'Bandwidth':
        src = "/assets/contour/stress vs bandwidth.png"
    elif xaxis_value == 'Stress' and yaxis_value == 'Strain':
        src = "/assets/contour/stress vs strain.png"
    elif xaxis_value == 'Stress' and yaxis_value == 'Stress':
        src = "/assets/contour/stress vs stress.png"
    elif xaxis_value == 'Stress' and yaxis_value == 'Efficiency':
        src = "/assets/contour/stress vs efficiency.png"
    elif xaxis_value == 'Stress' and yaxis_value == 'Power Density':
        src = "/assets/contour/stress vs power density.png"
    elif xaxis_value == 'Efficiency' and yaxis_value == 'Bandwidth':
        src = "/assets/contour/efficiency vs bandwidth.png"
    elif xaxis_value == 'Efficiency' and yaxis_value == 'Strain':
        src = "/assets/contour/efficiency vs strain.png"
    elif xaxis_value == 'Efficiency' and yaxis_value == 'Stress':
        src = "/assets/contour/efficiency vs stress.png"
    elif xaxis_value == 'Efficiency' and yaxis_value == 'Efficiency':
        src = "/assets/contour/efficiency vs efficiency.png"
    elif xaxis_value == 'Efficiency' and yaxis_value == 'Power Density':
        src = "/assets/contour/efficiency vs power density.png"
    elif xaxis_value == 'Power Density' and yaxis_value == 'Bandwidth':
        src = "/assets/contour/power density vs bandwidth.png"
    elif xaxis_value == 'Power Density' and yaxis_value == 'Strain':
        src = "/assets/contour/power density vs strain.png"
    elif xaxis_value == 'Power Density' and yaxis_value == 'Stress':
        src = "/assets/contour/power density vs stress.png"
    elif xaxis_value == 'Power Density' and yaxis_value == 'Efficiency':
        src = "/assets/contour/power density vs efficiency.png"
    elif xaxis_value == 'Power Density' and yaxis_value == 'Power Density':
        src = "/assets/contour/power density vs power density.png"
    return src


# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)