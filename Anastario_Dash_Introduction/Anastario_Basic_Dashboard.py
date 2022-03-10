from dash import html, dcc, Dash, Input, Output, State
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

SIDEBAR_STYLE = {
    "top": "12rem",
    "position": "fixed",
    "left": 0,
    "bottom": 0,
    "width": "12rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "top": "2rem",
    "margin-left": "11rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

RE_STYLE = {
    "top": 0,
    "left": 0,
    "right" : 0,
    "bottom": 0,
}

HEADER_STYLE = {
    "top": 0,
    "left": 0,
    "bottom": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#93CAED",
}
jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("Jumbotron", className="display-3"),
            html.P(
                "404 Error",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "Something went wrong"
            ),
            html.P(
                dbc.Button("Learn more", color="primary"), className="lead"
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)
card = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(
                        src="/assets/portrait-placeholder.png",
                        className="img-fluid rounded-start",
                    ),
                    className="col-md-4",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H4("Nurse name", className="card-title"),
                            html.P(
                                "Description of nurse",
                                className="card-text",
                            ),
                            html.Small(
                                "Last updated 3 mins ago",
                                className="card-text text-muted",
                            ),
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3",
    style={"maxWidth": "540px"},
)

sidebar = html.Div([
    dbc.Nav([
        dbc.NavLink("Home", href="/", active="exact"),
        dbc.NavLink("Map", href="/page-1", active="exact"),
        dbc.NavLink("Setting", href="/page-2", active="exact"),
    ],
        vertical=True,
        pills=True,
    )
], style=SIDEBAR_STYLE)

header = html.Div([
    dbc.Row([
        html.H2("Nurse Dashboard", className="display-3"),
    ])
], style=HEADER_STYLE)

filters = html.Div([
    dbc.Row([
        dbc.Col(
            dbc.Button("Filter 1", outline=True, id='b1', n_clicks=0),
        ),
        dbc.Col(
            dbc.Button("Filter 2", outline=True, id='b2', n_clicks=0),
        ),
        dbc.Col(
            dbc.Button("Filter 3", outline=True, id='b3', n_clicks=0),
        ),
        dbc.Col(
            dbc.Button("Filter 4", outline=True, id='b4', n_clicks=0),
        ),
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label": "option 1", "value": "1"},
                            {"label": "option 2", "value": "2"},
                            {"label": "option 3", "value": "3"},
                        ]
                    ),
                ),
                id="c1",
                is_open=False,
            )
        ),
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label": "option 1", "value": "1"},
                            {"label": "option 2", "value": "2"},
                            {"label": "option 3", "value": "3"},
                        ]
                    ),
                ),
                id="c2",
                is_open=False,
            )
        ),
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label": "option 1", "value": "1"},
                            {"label": "option 2", "value": "2"},
                            {"label": "option 3", "value": "3"},
                        ]
                    ),
                ),
                id="c3",
                is_open=False,
            )
        ),
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label": "option 1", "value": "1"},
                            {"label": "option 2", "value": "2"},
                            {"label": "option 3", "value": "3"},
                        ]
                    ),
                ),
                id="c4",
                is_open=False,
            )
        ),
    ])
])

aa = [dbc.Container([
    dbc.Row([
        html.Div([
            dcc.Dropdown(
                id="Name",
                options=[
                    {"label": "Sample Nurse 1", "value": "Sample Nurse 1"},
                    {"label": "Sample Nurse 2", "value": "Sample Nurse 2"},
                    {"label": "Sample Nurse 3", "value": "Sample Nurse 3"},
                    {"label": "Sample Nurse 4", "value": "Sample Nurse 4"},
                ],
                multi=True,
                placeholder="search for nurse by name",
            )
        ]),
    ]),
    filters,
    dbc.Row([
        dbc.Col(dbc.Card(
            [
                dbc.CardHeader("Nurse"),
                dbc.CardBody(
                    [
                        html.H5("Nurse 1", className="card-title"),
                        html.P(
                            "This is some card content that we'll reuse",
                            className="card-text",
                        ),
                        dbc.Button(
                            "Detail", id="nurse1", color="secondary", className="mt-auto", n_clicks=0
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Nurse 1"), close_button=True),
                                dbc.ModalBody(card),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Close",
                                        id="close-nurse1",
                                        className="ms-auto",
                                        n_clicks=0,
                                    )
                                ),
                            ],
                            id="modal-nurse1",
                            is_open=False,
                        ),
                    ]
                ),
            ],
            color="primary",
            outline=True,
        )),
        dbc.Col(dbc.Card(
            [
                dbc.CardHeader("Nurse"),
                dbc.CardBody(
                    [
                        html.H5("Nurse 2", className="card-title"),
                        html.P(
                            "This is some card content that we'll reuse",
                            className="card-text",
                        ),
                        dbc.Button(
                            "Detail", id="nurse2", color="secondary", className="mt-auto", n_clicks=0
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Nurse 2"), close_button=True),
                                dbc.ModalBody(card),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Close",
                                        id="close-nurse2",
                                        className="ms-auto",
                                        n_clicks=0,
                                    )
                                ),
                            ],
                            id="modal-nurse2",
                            is_open=False,
                        ),
                    ]
                ),
            ],
            color="primary",
            outline=True,
        )),
        dbc.Col(dbc.Card(
            [
                dbc.CardHeader("Nurse"),
                dbc.CardBody(
                    [
                        html.H5("Nurse 3", className="card-title"),
                        html.P(
                            "This is some card content that we'll reuse",
                            className="card-text",
                        ),
                        dbc.Button(
                            "Detail", id="nurse3", color="secondary", className="mt-auto", n_clicks=0
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Nurse 3"), close_button=True),
                                dbc.ModalBody(card),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Close",
                                        id="close-nurse3",
                                        className="ms-auto",
                                        n_clicks=0,
                                    )
                                ),
                            ],
                            id="modal-nurse3",
                            is_open=False,
                        ),
                    ]
                ),
            ],
            color="primary",
            outline=True,
        ))
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col(dbc.Card(
            [
                dbc.CardHeader("Nurse"),
                dbc.CardBody(
                    [
                        html.H5("Nurse 4", className="card-title"),
                        html.P(
                            "This is some card content that we'll reuse",
                            className="card-text",
                        ),
                        dbc.Button(
                            "Detail", id="nurse4", color="secondary", className="mt-auto", n_clicks=0
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Nurse 4"), close_button=True),
                                dbc.ModalBody(card),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Close",
                                        id="close-nurse4",
                                        className="ms-auto",
                                        n_clicks=0,
                                    )
                                ),
                            ],
                            id="modal-nurse4",
                            is_open=False,
                        ),
                    ]
                ),
            ],
            color="primary",
            outline=True,
        )),
        dbc.Col(dbc.Card(
            [
                dbc.CardHeader("Nurse"),
                dbc.CardBody(
                    [
                        html.H5("Nurse 5", className="card-title"),
                        html.P(
                            "This is some card content that we'll reuse",
                            className="card-text",
                        ),
                        dbc.Button(
                            "Detail", id="nurse5", color="secondary", className="mt-auto", n_clicks=0
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Nurse 1"), close_button=True),
                                dbc.ModalBody(card),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Close",
                                        id="close-nurse5",
                                        className="ms-auto",
                                        n_clicks=0,
                                    )
                                ),
                            ],
                            id="modal-nurse5",
                            is_open=False,
                        ),
                    ]
                ),
            ],
            color="primary",
            outline=True,
        )),
        dbc.Col(dbc.Card(
            [
                dbc.CardHeader("Nurse"),
                dbc.CardBody(
                    [
                        html.H5("Nurse 6", className="card-title"),
                        html.P(
                            "This is some card content that we'll reuse",
                            className="card-text",
                        ),
                        dbc.Button(
                            "Detail", id="nurse6", color="secondary", className="mt-auto", n_clicks=0
                        ),
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Nurse 1"), close_button=True),
                                dbc.ModalBody(card),
                                dbc.ModalFooter(
                                    dbc.Button(
                                        "Close",
                                        id="close-nurse6",
                                        className="ms-auto",
                                        n_clicks=0,
                                    )
                                ),
                            ],
                            id="modal-nurse6",
                            is_open=False,
                        ),
                    ]
                ),
            ],
            color="primary",
            outline=True,
        ))
    ])
], fluid=True)]
content = html.Div(aa, id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([
    dcc.Location(id="url"),
    header,
    sidebar,
    content
])


# callbacks
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


@app.callback(
    Output("modal-nurse1", "is_open"),
    [Input("nurse1", "n_clicks"), Input("close-nurse1", "n_clicks")],
    [State("modal-nurse1", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("modal-nurse2", "is_open"),
    [Input("nurse2", "n_clicks"), Input("close-nurse2", "n_clicks")],
    [State("modal-nurse2", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("modal-nurse3", "is_open"),
    [Input("nurse3", "n_clicks"), Input("close-nurse3", "n_clicks")],
    [State("modal-nurse3", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("modal-nurse4", "is_open"),
    [Input("nurse4", "n_clicks"), Input("close-nurse4", "n_clicks")],
    [State("modal-nurse4", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("modal-nurse5", "is_open"),
    [Input("nurse5", "n_clicks"), Input("close-nurse5", "n_clicks")],
    [State("modal-nurse5", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("modal-nurse6", "is_open"),
    [Input("nurse6", "n_clicks"), Input("close-nurse6", "n_clicks")],
    [State("modal-nurse6", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page(pathname):
    if pathname == "/":
        return aa
    elif pathname == "/page-1":
        return [
            html.H5("Map")
        ]
    elif pathname == "/page-2":
        return [
            html.H5("Setting")
        ]
    return [jumbotron]


if __name__ == '__main__':
    app.run_server(debug=True)
