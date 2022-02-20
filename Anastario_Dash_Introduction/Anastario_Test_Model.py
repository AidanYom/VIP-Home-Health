from dash import html, dcc, Dash, Input, Output, State
import dash_bootstrap_components as dbc
# import pandas as pd
# import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

SIDEBAR_STYLE = {
    "top": "12rem",
    "position":"fixed",
    "left": 0,
    "bottom": 0,
    "width": "10rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "top": "2rem",
    "margin-left": "11rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

HEADER_STYLE = {
    "top": 0,
    "left": 0,
    "bottom": "2rem",
    "padding": "2rem 1rem",
    "background-color":"#93CAED",
}


sidebar = html.Div([
    dbc.Row([
        dbc.Col(children=[
            dbc.Row(html.Div("Home")),
            dbc.Row(html.Div("Settings")),
            dbc.Row(html.Div("Buttons...")),
            ],
            width={'order':'first', 'size':1}
        ),
    ])
], style=SIDEBAR_STYLE)

header = html.Div([
    dbc.Row([
        html.H2("Nurse Dashboard", className="display-3"),
    ])
], style=HEADER_STYLE)

filters = html.Div([
    dbc.Row([
        dbc.Col(
            dbc.Button("Filter 1", outline = True, id='b1', n_clicks=0),
        ),
        dbc.Col(
            dbc.Button("Filter 2", outline = True, id='b2', n_clicks=0),
        ),
        dbc.Col(
            dbc.Button("Filter 3", outline = True, id='b3', n_clicks=0),
        ),
        dbc.Col(
            dbc.Button("Filter 4", outline = True, id='b4', n_clicks=0),
        ),
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label":"option 1", "value":"1"},
                            {"label":"option 2", "value":"2"},
                            {"label":"option 3", "value":"3"},
                        ]
                    ),
                ),
                id = "c1",
                is_open=False,
            )
        ),
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label":"option 1", "value":"1"},
                            {"label":"option 2", "value":"2"},
                            {"label":"option 3", "value":"3"},
                        ]
                    ),
                ),
                id = "c2",
                is_open=False,
            )
        ),
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label":"option 1", "value":"1"},
                            {"label":"option 2", "value":"2"},
                            {"label":"option 3", "value":"3"},
                        ]
                    ),
                ),
                id = "c3",
                is_open=False,
            )
        ),
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label":"option 1", "value":"1"},
                            {"label":"option 2", "value":"2"},
                            {"label":"option 3", "value":"3"},
                        ]
                    ),
                ),
                id = "c4",
                is_open=False,
            )
        ),
    ])
])

content = html.Div([dbc.Container([
    dbc.Row([
        html.Div([
            dcc.Dropdown(
                id="Name",
                options=[
                    {"label":"Sample Nurse 1", "value":"Sample Nurse 1"},
                    {"label":"Sample Nurse 2", "value":"Sample Nurse 2"},
                    {"label":"Sample Nurse 3", "value":"Sample Nurse 3"},
                    {"label":"Sample Nurse 4", "value":"Sample Nurse 4"},
                ],
                multi=True,
                placeholder = "search for nurse by name",
            )
        ]),
    ]),
    filters,
    #dbc.Row([
        # dbc.Col(html.Div([html.H3("Nurse")]), width={'size':6}),
        # dbc.Col(html.Div([html.H3("Number of Patients")]), width={'size':3}),


    #]),
    dbc.Row([
        # dbc.Accordion([
        #     dbc.AccordionItem([
        #         html.P("Nurse information"),
        #         html.P("more info")  
        #     ], title="Sample Nurse 1"),
        #     dbc.AccordionItem([
        #         html.P("Nurse information"),
        #         html.P("more info") 
        #     ], title="Sample Nurse 2"),
        #     dbc.AccordionItem([
        #         html.P("Nurse information"),
        #         html.P("more info")  
        #     ], title="Sample Nurse 3"),
        #     dbc.AccordionItem([
        #         html.P("Nurse information"),
        #         html.P("more info")  
        #     ], title="Sample Nurse 4"),
        # ],
        # flush=True)
    ])
], fluid=True)], style=CONTENT_STYLE)

app.layout = html.Div([
    header,
    sidebar,
    content
])

#callbacks
@app.callback(
    Output("c1", "is_open"),
    Input("b1", "n_clicks"),
    [State("c1", "is_open")],
)
def toggle_left(n_b1, is_open):
    if n_b1:
        return not is_open
    return is_open

@app.callback(
    Output("c2", "is_open"),
    Input("b2", "n_clicks"),
    [State("c2", "is_open")],
)
def toggle_left(n_b2, is_open):
    if n_b2:
        return not is_open
    return is_open

@app.callback(
    Output("c3", "is_open"),
    Input("b3", "n_clicks"),
    [State("c3", "is_open")],
)
def toggle_left(n_b3, is_open):
    if n_b3:
        return not is_open
    return is_open

@app.callback(
    Output("c4", "is_open"),
    Input("b4", "n_clicks"),
    [State("c4", "is_open")],
)
def toggle_left(n_b4, is_open):
    if n_b4:
        return not is_open
    return is_open



if __name__ == '__main__':
    app.run_server(debug = True)