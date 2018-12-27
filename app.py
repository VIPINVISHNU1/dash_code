## Evolving from the basics

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

all_options = {
    'Target': ['FMSA_EEJ_TRUNK_NT', '091-9156-6F0001G_NT', '091-9156-1E0003A_NT'],
    'Host': ['FMSA_EEJ_TRUNK_NT', '091-9156-6F0001G_NT', 'FMSA_EEJ_091-9156-1E0003A_NT','FMSA_CSERIES_INT_NT'],
    'All': ['FMSA_EEJ_TRUNK_NT', '091-9156-6F0001G_NT', '091-9156-1E0003A_NT','FMSA_EEJ_091-9156-1E0003A_NT', '091-9156-6F0001G_NT', 'FMSA_EEJ_091-9156-1E0003A_NT','FMSA_CSERIES_INT_NT']
}

build_data = {
    'FMSA_EEJ_TRUNK_NT': {'x': [1, 2, 3], 'y': [4, 1, 2]},
    '091-9156-6F0001G_NT': {'x': [1, 2, 3], 'y': [2, 4, 5]},
    '091-9156-1E0003A_NT': {'x': [1, 2, 3], 'y': [2, 2, 7]},
    'FMSA_EEJ_091-9156-1E0003A_NT': {'x': [1, 2, 3], 'y': [1, 0, 2]},
    '091-9156-6F0001G_NT': {'x': [1, 2, 3], 'y': [4, 7, 3]},
    'FMSA_CSERIES_INT_NT': {'x': [1, 2, 3], 'y': [2, 3, 3]}
}

# Boostrap CSS.
app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})  # noqa: E501

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(children='FARM-MATRIX',
                        className='nine columns'),
                #html.Img(
                #    src="http://static1.squarespace.com/static/546fb494e4b08c59a7102fbc/t/591e105a6a496334b96b8e47/1497495757314/.png",
                #    className='three columns',
                #    style={
                #        'height': '9%',
                #        'width': '9%',
                #        'float': 'right',
                #        'position': 'relative',
                #        'padding-top': 0,
                #        'padding-right': 0
                #    },
                #),
                html.Div(children='''
                        A web application for Target matrix.
                        ''',
                        className='nine columns'
                )
            ], className="row"
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose Build:'),
                        dcc.Checklist(
                                id = 'builds',
                                options=[
                                    {'label': 'FMSA_EEJ_TRUNK_NT', 'value': 'FMSA_EEJ_TRUNK_NT'},
                                    {'label': '091-9156-6F0001G_NT', 'value': '091-9156-6F0001G_NT'}
                                ],
                                values=['FMSA_EEJ_TRUNK_NT', '091-9156-6F0001G_NT'],
                                labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),
                html.Div(
                    [
                        html.P('Choose Platform:'),
                        dcc.RadioItems(
                                id = 'Platform',
                                options=[{'label': k, 'value': k} for k in all_options.keys()],
                                value='All',
                                labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                )
            ], className="row"
        ),

        html.Div(
            [
            html.Div([
                    dcc.Graph(
                        id='example-graph',
                        config={"displaylogo": False},
                    )
                ], className= 'six columns'
                ),

                html.Div([
                    dcc.Graph(
                        id='example-graph-2',config={
                                "displaylogo": False},
                    )
                ], className= 'six columns'
                )
            ], className="row"
        )
    ], className='ten columns offset-by-one')
)
@app.callback(
    dash.dependencies.Output('builds', 'options'),
    [dash.dependencies.Input('Platform', 'value')])
def set_builds_options(selected_platform):
    return [{'label': i, 'value': i} for i in all_options[selected_platform]]

@app.callback(
    dash.dependencies.Output('example-graph', 'figure'),
    [dash.dependencies.Input('builds', 'values')])
def update_image_src(selector):
    data = []
    for build in selector:
        data.append({'x': build_data[build]['x'], 'y': build_data[build]['y'],
                    'type': 'bar', 'name': build})
    figure = {
        'data': data,
        'layout': {
            'title': 'Graph 1',
            'xaxis' : dict(
                title='x Axis',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='y Axis',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

@app.callback(
    dash.dependencies.Output('example-graph-2', 'figure'),
    [dash.dependencies.Input('builds', 'values')])
def update_image_src(selector):
    data = []
    for build in selector:
        data.append({'x': build_data[build]['x'], 'y': build_data[build]['y'],
                    'type': 'line', 'name':build})
    figure = {
        'data': data,
        'layout': {
            'title': 'Graph 2',
            'xaxis' : dict(
                title='x Axis',
                titlefont=dict(
                family='Courier New, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='y Axis',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, threaded=True)