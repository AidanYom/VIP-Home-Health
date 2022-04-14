from turtle import width, xcor
from dash import html, dcc, Dash, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import dash_auth

# make sample data to read from
nurse_data = {'Name': ['Jack Knox', 'Hanna Ertel', 'Aidan Anastario', 'Kaushik Karthik', 'Miranda Chai', 'Jay Kee'],
              'Area': ['Queens', 'Staten Island', 'Bronx', 'Manhattan', 'Queens', 'Brooklyn'],
              'Num_Patients': [5, 4, 5, 5, 3, 6],
              'Hospis': [0, 0, 1, 0, 1, 1],
              'Traich': [1, 1, 0, 0, 0, 0],
              'Colostony': [1, 0, 1, 1, 1, 0]
              }
patient_data = {'Name': ['Patient A', 'Patient B', 'Patient C', 'Patient D', 'Patient E', 'Patient F'],
              'Area': ['Queens', 'Staten Island', 'Bronx', 'Manhattan', 'Queens', 'Brooklyn'],
        'assigned_nurse':['Jack Knox', 'Hanna Ertel', 'Aidan Anastario', 'Kaushik Karthik', 'Miranda Chai', 'Jay Kee'],
              'Cold': [0, 0, 1, 0, 1, 1],
              'COVID': [1, 1, 0, 0, 0, 0],
              'Headache': [1, 0, 1, 1, 1, 0]
              }


nurse_df = pd.DataFrame(nurse_data)
nurse_info_list = []

patient_df = pd.DataFrame(patient_data)
patient_info_list = []

for x in range(0, len(nurse_df)):
    nurse_info_list.append([])
    nurse_info_list[x].append(nurse_df.at[x, 'Name'])
    nurse_info_list[x].append(nurse_df.at[x, 'Area'])
    nurse_info_list[x].append(str(nurse_df.at[x, 'Num_Patients']))
    if (nurse_df.at[x, 'Hospis'] == 1):
        nurse_info_list[x].append("Hospis")
    else:
        nurse_info_list[x].append(0)
    if (nurse_df.at[x, 'Traich'] == 1):
        nurse_info_list[x].append("Traich")
    else:
        nurse_info_list[x].append(0)
    if (nurse_df.at[x, 'Colostony'] == 1):
        nurse_info_list[x].append("Colostony")
    else:
        nurse_info_list[x].append(0)

for x in range(0, len(patient_df)):
    patient_info_list.append([])
    patient_info_list[x].append(patient_df.at[x, 'Name'])
    patient_info_list[x].append(patient_df.at[x, 'Area'])
    patient_info_list[x].append(patient_df.at[x, 'assigned_nurse'])
    if (patient_df.at[x, 'Cold'] == 1):
        patient_info_list[x].append("Cold")
    else:
        patient_info_list[x].append(0)
    if (patient_df.at[x, 'COVID'] == 1):
        patient_info_list[x].append("COVID")
    else:
        patient_info_list[x].append(0)
    if (patient_df.at[x, 'Headache'] == 1):
        patient_info_list[x].append("Headache")
    else:
        patient_info_list[x].append(0)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# add a mobile layout component later

auth = dash_auth.BasicAuth(
    app,
    {'ID': 'password',
     'ID2': 'password2'}
)

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

sidebar = html.Div([
    dbc.Nav([
        dbc.NavLink("Home", href="/", active="exact"),
        dbc.NavLink("Patient", href="/page-1", active="exact"),
        dbc.NavLink("Setting", href="/page-2", active="exact"),
    ],
        vertical=True,
        pills=True,
    )
])

header = dbc.Container([
    dbc.Row([
        html.H1("Nurse Dashboard", className="text-center text-secondary"),
    ])
])
# redo the filters to be a search by name and one collapse with filters displayed
aa = [dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id="Name",
                options=[
                    {"label": x, "value": x}
                    for x in sorted(nurse_df['Name'])
                ],
                multi=True,
                placeholder="search for nurse by name",
            )
        ], width={"size": 3}),
        dbc.Col(
            dbc.Button("Area", outline=True, id='area_filter', n_clicks=0),
            width={"size": 2},
            align='start'
        ),
        dbc.Col(
            dbc.Button("# Patients", outline=True, id='num_patients_filter', n_clicks=0),
            width={"size": 2},
            align='start'
        ),
        dbc.Col(
            dbc.Button("Skills", outline=True, id='skills_filter', n_clicks=0),
            width={"size": 5},
            align='start'
        ),
    ], justify='start', className="g-0"),
    dbc.Row([
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label": x, "value": x}
                            for x in sorted(nurse_df["Area"].unique())
                        ],
                        id="area_filter_checklist",
                    ),
                ),
                id="area_collapse",
                is_open=False,
            ),
            width={'size': 2, 'offset': 3},
        ),
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label": x, "value": x}
                            for x in sorted(nurse_df["Num_Patients"].unique())
                        ],
                        id="num_patients_checklist",
                    ),
                ),
                id="num_patients_collapse",
                is_open=False,
            ),
            width={'size': 2},
        ),
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label": "Hospis", "value": "Hospis"},
                            {"label": "Traich", "value": "Traich"},
                            {"label": "Colostony", "value": "Colostony"},
                        ],
                        id="skills_filter_checklist"
                    ),
                ),
                id="skills_collapse",
                is_open=False,
            ),
            width={'size': 2},
        ),

    ], align='start'),
    html.Br(),
    dbc.Row([
        dbc.ListGroup([
            html.Div(id='nurse_group_list', children=[])
        ])
    ])
], fluid=True)]

bb = [dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id="patient_Name",
                options=[
                    {"label": x, "value": x}
                    for x in sorted(patient_df['Name'])
                ],
                multi=True,
                placeholder="search for patient by name",
            )
        ], width={"size": 3}),
        dbc.Col(
            dbc.Button("Area", outline=True, id='patient_area_filter', n_clicks=0),
            width={"size": 2},
            align='start'
        ),
        dbc.Col(
            dbc.Button("Assigned Nurse", outline=True, id='assigned_nurse_filter', n_clicks=0),
            width={"size": 2},
            align='start'
        ),
        dbc.Col(
            dbc.Button("Symptoms/Disease", outline=True, id='sd_filter', n_clicks=0),
            width={"size": 5},
            align='start'
        ),
    ], justify='start', className="g-0"),
    dbc.Row([
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label": x, "value": x}
                            for x in sorted(patient_df["Area"].unique())
                        ],
                        id="patient_area_filter_checklist",
                    ),
                ),
                id="patient_area_collapse",
                is_open=False,
            ),
            width={'size': 2, 'offset': 3},
        ),
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label": x, "value": x}
                            for x in sorted(patient_df["assigned_nurse"].unique())
                        ],
                        id="assigned_nurse_checklist",
                    ),
                ),
                id="assigned_nurse_collapse", #num_patients_collapse
                is_open=False,
            ),
            width={'size': 2},
        ),
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label": "Cold", "value": "Cold"},
                            {"label": "COVID", "value": "COVID"},
                            {"label": "Headache", "value": "Headache"},
                        ],
                        id="sd_filter_checklist" #skills_filter_checklist
                    ),
                ),
                id="sd_collapse", #skills_collapse
                is_open=False,
            ),
            width={'size': 2},
        ),

    ], align='start'),
    html.Br(),
    dbc.Row([
        dbc.ListGroup([
            html.Div(id='patient_group_list', children=[]) #nurse_group_list
        ])
    ])
], fluid=True)]

content = html.Div(aa, id="page-content")

app.layout = dbc.Container([
    dcc.Location(id="url"),
    header,
    html.Br(),
    dbc.Row([
        dbc.Col([
            sidebar
        ], width={'size': 1}),
        dbc.Col([content], width={'size': 11}),
    ])
], fluid=True)


# nurse page callbacks
@app.callback(
    Output('nurse_group_list', 'children'),
    [Input('Name', 'value'),
     Input('area_filter_checklist', 'value'),
     Input('num_patients_checklist', 'value'),
     Input('skills_filter_checklist', 'value')]
)
def nurse_filter_list(name_list, area_list, num_patients_list, skills_list):
    filtered_list = []
    for x in nurse_info_list:
        selected = True
        if (name_list is not None and len(name_list) > 0):
            if (not (x[0] in name_list)):
                selected = False
        if (area_list is not None and len(area_list) > 0):
            if (not (x[1] in area_list)):
                selected = False
        if (num_patients_list is not None and len(num_patients_list) > 0):
            if (not (int(x[2]) in num_patients_list)):
                selected = False
        if (skills_list is not None and len(skills_list) > 0):
            for y in skills_list:
                if (not ((x[3] == y) | (x[4] == y) | (x[5] == y))):
                    selected = False
        if (selected):
            filtered_list.append(dbc.ListGroupItem(dbc.Row(
                (dbc.Col(x[0], width={'size': 3}),
                 dbc.Col(x[1], width={'size': 2}),
                 dbc.Col(x[2], width={'size': 2}),
                 dbc.Col(x[3], width={'size': 1}) if x[3] != 0 else dbc.Col("", width={'size': 1}),
                 dbc.Col(x[4], width={'size': 1}) if x[4] != 0 else dbc.Col("", width={'size': 1}),
                 dbc.Col(x[5], width={'size': 1}) if x[5] != 0 else dbc.Col("", width={'size': 1})),
                className='gx-5',
            )))

    return filtered_list


# basic
@app.callback(
    Output("area_collapse", "is_open"),
    Input("area_filter", "n_clicks"),
    [State("area_collapse", "is_open")],
)
def nurse_toggle_left(n_area_filter, is_open):
    if n_area_filter:
        return not is_open
    return is_open


@app.callback(
    Output("num_patients_collapse", "is_open"),
    Input("num_patients_filter", "n_clicks"),
    [State("num_patients_collapse", "is_open")],
)
def nurse_toggle_left(n_num_patients_filter, is_open):
    if n_num_patients_filter:
        return not is_open
    return is_open


@app.callback(
    Output("skills_collapse", "is_open"),
    Input("skills_filter", "n_clicks"),
    [State("skills_collapse", "is_open")],
)
def nurse_toggle_left(n_skills_filter, is_open):
    if n_skills_filter:
        return not is_open
    return is_open

# patient page callbacks
@app.callback(
    Output('patient_group_list', 'children'),
    [Input('patient_Name', 'value'),
     Input('patient_area_filter_checklist', 'value'),
     Input('assigned_nurse_checklist', 'value'),
     Input('sd_filter_checklist', 'value')]
)
def patient_filter_list(name_list, area_list, num_patients_list, skills_list):
    filtered_list = []
    for x in patient_info_list:
        selected = True
        if (name_list is not None and len(name_list) > 0):
            if (not (x[0] in name_list)):
                selected = False
        if (area_list is not None and len(area_list) > 0):
            if (not (x[1] in area_list)):
                selected = False
        if (num_patients_list is not None and len(num_patients_list) > 0):
            if (not ((x[2]) in num_patients_list)):
                selected = False
        if (skills_list is not None and len(skills_list) > 0):
            for y in skills_list:
                if (not ((x[3] == y) | (x[4] == y) | (x[5] == y))):
                    selected = False
        if (selected):
            filtered_list.append(dbc.ListGroupItem(dbc.Row(
                (dbc.Col(x[0], width={'size': 3}),
                 dbc.Col(x[1], width={'size': 2}),
                 dbc.Col(x[2], width={'size': 2}),
                 dbc.Col(x[3], width={'size': 1}) if x[3] != 0 else dbc.Col("", width={'size': 1}),
                 dbc.Col(x[4], width={'size': 1}) if x[4] != 0 else dbc.Col("", width={'size': 1}),
                 dbc.Col(x[5], width={'size': 1}) if x[5] != 0 else dbc.Col("", width={'size': 1})),
                className='gx-5',
            )))

    return filtered_list


# basic
@app.callback(
    Output("patient_area_collapse", "is_open"),
    Input("patient_area_filter", "n_clicks"),
    [State("patient_area_collapse", "is_open")],
)
def patient_toggle_left(n_area_filter, is_open):
    if n_area_filter:
        return not is_open
    return is_open


@app.callback(
    Output("assigned_nurse_collapse", "is_open"),
    Input("assigned_nurse_filter", "n_clicks"),
    [State("assigned_nurse_collapse", "is_open")],
)
def patient_toggle_left(n_assigned_nurse, is_open):
    if n_assigned_nurse:
        return not is_open
    return is_open


@app.callback(
    Output("sd_collapse", "is_open"),
    Input("sd_filter", "n_clicks"),
    [State("sd_collapse", "is_open")],
)
def patient_toggle_left(n_skills_filter, is_open):
    if n_skills_filter:
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
        return bb
    elif pathname == "/page-2":
        return [
            html.H5("Setting")
        ]
    return [jumbotron]


if __name__ == '__main__':
    app.run_server(debug=True)
