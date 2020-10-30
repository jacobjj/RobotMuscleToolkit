import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.graph_objects as go

from app import app
import os
import sys
import logging

import sklearn
import numpy as np
import pickle as pkl

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#read csv
df = pd.read_csv('data.csv')

# remove SMP actuator types 
df = df[df['Actuator Type'] != 'SMP']
df = df[df['Actuator Type'] != 'TSA']

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
                                    'class, with the classes of actuators being PZT, DEA, IPMC, SMA, SFA, SCP, and '
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
            id='x_dropdown',
            options=[
                {'label': 'Bandwidth (Hz)', 'value': 'Bandwidth'},
                {'label': 'Strain (%)', 'value': 'Strain'},
                {'label': 'Stress (MPa)', 'value': 'Stress'},
                {'label': 'Efficiency (%)', 'value': 'Efficiency'},
                {'label': 'Power Density (W/g)', 'value': 'PowerDensity'}
            ],
            value='Strain',
            style={'width': '48%', 'display': 'inline-block'}
        ),
        dcc.Dropdown(
            id='y_dropdown',
            options=[
                {'label': 'Bandwidth (Hz)', 'value': 'Bandwidth'},
                {'label': 'Strain (%)', 'value': 'Strain'},
                {'label': 'Stress (MPa)', 'value': 'Stress'},
                {'label': 'Efficiency (%)', 'value': 'Efficiency'},
                {'label': 'Power Density (W/g)', 'value': 'PowerDensity'}
            ],
            value='Stress',
            style={'width': '48%', 'float': 'right', 'display': 'inline-block'}
        ),
        dcc.Graph(id='contour-plot',
                figure={
                    "layout": {
                    "title": "Actuator Properties",
                    "height": 750,  # px

        }}),
        dbc.Row([
            dbc.Col(html.A(children='')
                , className="mb-5")
        ]),
        dbc.Row([
            dbc.Col(html.A(children='Input your x and y parameters below to determine which actuator type is best for you '
                                    '(We will transform your parameters and run them against our classifier before '
                                    'the point is plotted): ')
                , className="mb-5")
        ]),
        dcc.Input(
            id="x_input".format(),
            type="number",
            placeholder="X Parameter".format(),
            style={'float': 'left','display': 'inline-block'}
        ),
        dcc.Input(
            id="y_input".format(),
            type="number",
            placeholder="Y Parameter".format(),
            style={'float': 'right', 'display': 'inline-block'}
        ),
        dbc.Row([
            dbc.Col(html.P(children='')
                , className="mb-5")
        ]),
        dbc.Button('Clear', id='clear-plot', n_clicks=0, style={
            'width':'10%', 'float':'right', 'margin-left': '15px', 'background-color': '#e0e0e0'
        }), 
        dbc.Button('Plot', id='plot-vals', n_clicks=0, style={
            'width':'10%', 'float':'right', 'font-weight': 'bold', 'background-color': '#e0f0e3'
        }),
        dbc.Row([
            dbc.Col(html.P(children='')
                , className="mb-5")
        ]),
        html.Div(id='return_actuator_type',
             children=''),
        dbc.Row([
            dbc.Col(html.P(children='')
                , className="mb-5")
        ]),
        # dbc.Row([
        #     dbc.Col(html.A(children='Input your available parameters and we will use our imputer to fill in the missing '
        #                             'values and our classifier to predict which actuator type you should use. ')
        #         , className="mb-5")
        # ]),
        # dcc.Input(
        #     id="bandwidth_input".format(),
        #     type="number",
        #     placeholder="Bandwidth".format(),
        #     style={'display': 'inline-block', 'margin-right': '10px'}
        # ),
        # dcc.Input(
        #     id="strain_input".format(),
        #     type="number",
        #     placeholder="Strain".format(),
        #     style={'display': 'inline-block', 'margin-right': '10px'}
        # ),
        # dcc.Input(
        #     id="stress_input".format(),
        #     type="number",
        #     placeholder="Stress".format(),
        #     style={'display': 'inline-block', 'margin-right': '10px'}
        # ),
        # dcc.Input(
        #     id="efficiency_input".format(),
        #     type="number",
        #     placeholder="Efficiency".format(),
        #     style={'display': 'inline-block', 'margin-right': '10px'}
        # ),
        # dcc.Input(
        #     id="powerDensity_input".format(),
        #     type="number",
        #     placeholder="Power Density".format(),
        #     style={'display': 'inline-block', 'margin-right': '10px'}
        # ),
        # dbc.Button('Submit', id='input-features', n_clicks=0, style={
        #     'width':'10%', 'float':'right', 'font-weight': 'bold', 'background-color': '#e0f0e3'
        # }),
        # html.Div(id='return_missing_vals',
        #      children=''),
        dbc.Row([
            dbc.Col(html.P(children='')
                , className="mb-5")
        ]),
    ])
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value')])

#updates x and y values based on dropdown and indicates each dot by actuator type
def update_graph(xaxis_column_name, yaxis_column_name):
    ticklabels = {}
    ticklabels['Bandwidth (Hz)'] = np.log10([0.01, 1, 100, 1e4, 1e6])
    ticklabels['Strain (%)'] = np.log10([0.001, 0.1, 10, 1000, 1e5]) 
    ticklabels['Stress (MPa)'] = np.log10([0.1, 1, 10, 100, 1000, 10000])
    ticklabels['Efficiency (%)'] = np.log10([0.01, 0.1, 1, 10, 100, 1000] ) 
    ticklabels['Power Density (W/g)'] = np.log10([1e-7, 0.0001, 0.1, 100, 1e5])

    xlabels = list(ticklabels.get(xaxis_column_name))
    ylabels = list(ticklabels.get(yaxis_column_name))

    ticktext = {}
    ticktext['Bandwidth (Hz)'] = [0.01, 1, 100, 1e4, 1e6]
    ticktext['Strain (%)'] = [0.001, 0.1, 10, 1000, 1e5]
    ticktext['Stress (MPa)'] = [0.1, 1, 10, 100, 1000, 10000]
    ticktext['Efficiency (%)'] = [0.01, 0.1, 1, 10, 100, 1000] 
    ticktext['Power Density (W/g)'] = [1e-7, 0.0001, 0.1, 100, 1e5]

    xtext = list(ticktext.get(xaxis_column_name))
    ytext = list(ticktext.get(yaxis_column_name)) 
    
    traces = []
    for i in df["Actuator Type"].unique():
        df_by_actuator = df[df['Actuator Type'] == i]
        traces.append(dict(
            x=np.log10(df_by_actuator[xaxis_column_name]),
            y=np.log10(df_by_actuator[yaxis_column_name]),
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
                'title': xaxis_column_name,
                'tickvals': xlabels, 
                'ticktext': xtext, 
                'zeroline': False,
                'range': (np.log10(df[xaxis_column_name].min()), np.log10(df[xaxis_column_name].max()))
            },
            yaxis={
                'title': yaxis_column_name, 
                'tickvals': ylabels, 
                'ticktext': ytext, 
                'zeroline': False, 
                'range': (np.log10(df[yaxis_column_name].min()), np.log10(df[yaxis_column_name].max()))
            },
            margin={'l': 80, 'b': 30, 't': 10, 'r': 0},
            legend={'x': 0.95, 'y': 0.95},
            hovermode='closest'
        )
    }

@app.callback(
    Output('contour-plot', 'figure'),
    [Input('plot-vals', 'n_clicks'),
    Input('clear-plot', 'n_clicks'),
    Input('x_dropdown', 'value'),
    Input('y_dropdown', 'value')],
    state = [dash.dependencies.State('x_input', 'value'),
    dash.dependencies.State('y_input', 'value')])

def graph_contour(plot_button, clear_button, x_dropdown, y_dropdown, x_input, y_input):
    ticklabels = {}
    ticklabels['Bandwidth'] = np.power(10., [-2, 0, 2, 4, 6])
    ticklabels['Strain'] = np.power(10., [-4, -2, 0, 2, 4]) 
    ticklabels['Stress'] = np.power(10., [-1, 0, 1, 2, 3, 4]) 
    ticklabels['Efficiency'] = np.power(10., [-2, -1, 0, 1, 2, 3]) 
    ticklabels['Power Density'] = np.power(10., [-7, -4, -1, 2, 5]) 

    xlabels = list(ticklabels.get(x_dropdown))
    ylabels = list(ticklabels.get(y_dropdown))

    ticktext = {}
    ticktext['Bandwidth'] = [0.01, 1, 100, 1e4, 1e6]
    ticktext['Strain'] = [0.0001, 0.01, 1, 100, 1e4]
    ticktext['Stress'] = [0.1, 1, 10, 100, 1000, 10000]
    ticktext['Efficiency'] = [0.01, 0.1, 1, 10, 100, 1000] 
    ticktext['Power Density'] = [1e-7, 0.0001, 0.1, 100, 1e5]

    xtext = list(ticktext.get(x_dropdown))
    ytext = list(ticktext.get(y_dropdown))

    path = os.path.join(os.getcwd(), 'assets/classifiers/{}_{}_scaler.pkl'.format(x_dropdown, y_dropdown))
    scaler = pkl.load(open(path, 'rb'))
    xticks = scaler.transform(np.stack([np.log(xlabels), np.ones_like(xlabels)], axis=1))[:, 0]
    yticks = scaler.transform(np.stack([np.ones_like(ylabels), np.log(ylabels)], axis=1))[:, 1]
    app.logger.info(xticks)
    xmin, xmax = xticks[[0, -1]]
    ymin, ymax = yticks[[0, -1]]

    layout = go.Layout(
    title="Actuator Properties",
    xaxis=dict(
        title=dropdown_label(x_dropdown),
        tickvals=xticks,
        ticktext=xtext,
        zeroline=False
    ),
    yaxis=dict(
        title=dropdown_label(y_dropdown),
        tickvals=yticks,
        ticktext=ytext,
        zeroline=False
    ))
    fig = go.Figure(layout=layout)
    fig.update_xaxes(range=[xmin, xmax])
    fig.update_yaxes(range=[ymin, ymax])

    fig.update_layout(
    autosize=False,
    width=700,
    height=700,
    )

    # Add images
    fig.add_layout_image(
        dict(
            source=app.get_asset_url('/contours/{}_{}.png'.format(x_dropdown, y_dropdown)),
            xref="x",
            yref="y",
            x=xmin,
            y=ymax,
            sizex=xmax - xmin,
            sizey=ymax - ymin,
            sizing="stretch",
            opacity=0.9,
            layer="below")
    )


    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'plot-vals' in changed_id:
        input_transformed = scaler.transform(np.asarray([[np.log(x_input), np.log(y_input)]]))[0]
        fig.add_trace(go.Scatter(x=[input_transformed[0]], y=[input_transformed[1]], mode='markers', 
        marker=dict(
            size=[16], color='white', opacity=1,
            line=dict(
                color='Red',
                width=4
            )
            )
        ))
    elif 'clear-plot' in changed_id:
        layout = go.Layout(
        title="Actuator Properties",
        xaxis=dict(
            title=dropdown_label(x_dropdown)
        ),
        yaxis=dict(
            title=dropdown_label(y_dropdown)
        ) ) 
        fig = go.Figure(layout=layout)

        fig.update_xaxes(range=[xmin, xmax])
        fig.update_yaxes(range=[ymin, ymax])

        if (x_dropdown == y_dropdown):
            return 'Please select two different parameters for plotting'
        else:
            # Add images
            fig.add_layout_image(
                dict(
                    source=app.get_asset_url('/contours/{}_{}.png'.format(x_dropdown, y_dropdown)),
                    xref="x",
                    yref="y",
                    x=xmin,
                    y=ymax,
                    sizex=xmax - xmin,
                    sizey=ymax - ymin,
                    sizing="stretch",
                    opacity=0.9,
                    layer="below")
            )


    # Set templates
    fig.update_layout(template="plotly_white")

    return fig

@app.callback(
    Output('return_actuator_type', 'children'),
    [Input('plot-vals', 'n_clicks'),
    Input('clear-plot', 'n_clicks'),
    Input('x_dropdown', 'value'),
    Input('y_dropdown', 'value')],
    state = [dash.dependencies.State('x_input', 'value'),
    dash.dependencies.State('y_input', 'value')])

def return_actuator(plot_button, clear_button, x_dropdown, y_dropdown, x_input, y_input):
    if (x_input or y_input) == None: 
        return ''
    if (x_input or y_input) == 0: 
        return 'Please enter a nonzero value.'
    filepath = os.path.join(os.getcwd(), 'assets/classifiers/{}_{}_.pkl'.format(x_dropdown, y_dropdown))
    clf = pkl.load(open(filepath, 'rb'))
    path = os.path.join(os.getcwd(), 'assets/classifiers/{}_{}_scaler.pkl'.format(x_dropdown, y_dropdown))
    scaler = pkl.load(open(path, 'rb'))
    X = np.log10(np.array([[x_input, y_input]]))
    X = scaler.transform(X)
    y = clf.decision_function(X.reshape(1, 2))
    app.logger.info(y)
    classes = ["PZT", "DEA", "IPMC", "SMA", "SCP", "SFA", "EAP"]
    sorted_y = np.argsort(y[0])
    y_0 = y[0]
    scores = sorted_y
    output = 'According to our classifier, these are the top three classes of actuators suitable for your use: ' + classes[sorted_y[6]] + ' with a confidence of ' + str(y_0[scores[6]])  + ', ' + classes[sorted_y[5]] + ' with a confidence of ' + str(y_0[scores[5]]) + ', ' + classes[sorted_y[4]] + ' with a confidence of ' + str(y_0[scores[4]])
    return output

# @app.callback(
#     Output('return_missing_vals', 'children'),
#     [Input('input-features', 'n_clicks'),
#     Input('bandwidth_input', 'value'),
#     Input('strain_input', 'value'),
#     Input('stress_input', 'value'),
#     Input('efficiency_input', 'value'),
#     Input('powerDensity_input', 'value')])

# def return_missing_features(submit, bandwidth, strain, stress, efficiency, powerDensity): 
#     changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
#     if 'input-features' in changed_id:
#         if (bandwidth or strain or stress or efficiency or powerDensity) == 0: 
#             return 'Please enter a nonzero value.'
#         if (bandwidth and strain and stress and efficiency and powerDensity == None):
#             return 'Please enter in a value'
#         if bandwidth == None: 
#             bandwidth = np.nan 
#         if strain == None: 
#             strain = np.nan
#         if stress == None: 
#             stress = np.nan
#         if efficiency == None: 
#             efficiency = np.nan 
#         if powerDensity == None: 
#             powerDensity = np.nan
#         X = [[bandwidth, strain, stress, efficiency, powerDensity]]
#         filepath = os.path.join(os.getcwd(), 'assets/classifiers/KNNmodel.pkl')
#         clf = pkl.load(open(filepath, 'rb'))
#         filepath_imputer = os.path.join(os.getcwd(), 'assets/classifiers/KNNimputer.pkl')
#         imputer = pkl.load(open(filepath_imputer, 'rb'))
#         imputed = imputer.transform(X)
#         imputed_log = np.log(imputed)
#         y = clf.predict(imputed_log)
#         classes = ["PZT", "DEA", "IPMC", "SMA", "SCP", "SFA", "TSA", "EAP"]
#         return 'Here are the data points with missing labels filled in: ' + str(imputed)  + '\n' + 'The actuator type you should use is: ' + classes[y[0]]
#     else: 
#         return 'Please enter at least one parameter to proceed'
        
        
def dropdown_label(dropdown_val):
    if dropdown_val == 'Strain':
        return 'Strain (%)'
    elif dropdown_val == 'Stress':
        return 'Stress (MPa)'
    elif dropdown_val == 'Efficiency':
        return 'Efficiency (%)'
    elif dropdown_val == 'Bandwidth':
        return 'Bandwidth (Hz)'
    elif dropdown_val == 'PowerDensity':
        return 'Power Density (W/g)'




# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)