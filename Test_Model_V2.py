from turtle import xcor
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

nurse_df = pd.DataFrame(nurse_data)

nurse_info_list = []

for x in range(0, len(nurse_df)):
    nurse_list_str = ''
    nurse_list_str += nurse_df.at[x, 'Name']
    for y in range(0, 30 - len(nurse_list_str)):
        nurse_list_str += " "
    nurse_list_str += nurse_df.at[x, 'Area']
    for y in range(0, 15 - len(nurse_df.at[x, 'Area'])):
        nurse_list_str += " "
    nurse_list_str += "         " + str(nurse_df.at[x, 'Num_Patients']) + "         "
    if (nurse_df.at[x, 'Hospis'] == 1):
        nurse_list_str += " Hospis"
    else:
        nurse_list_str += "       "
    nurse_list_str += "      "
    if (nurse_df.at[x, 'Traich'] == 1):
        nurse_list_str += " Traich"
    else:
        nurse_list_str += "       "
    nurse_list_str += "      "
    if (nurse_df.at[x, 'Colostony'] == 1):
        nurse_list_str += " Colonstrony"
    nurse_list_str += "      "
    nurse_info_list.append(nurse_list_str[0:(len(nurse_list_str) - 8)])

# [print(q) for q in nurse_info_list]

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
        dbc.NavLink("Map", href="/page-1", active="exact"),
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
            width={"size": 2}
        ),
        dbc.Col(
            dbc.Button("# Patients", outline=True, id='num_patients_filter', n_clicks=0),
            width={"size": 2}
        ),
        dbc.Col(
            dbc.Button("Skills", outline=True, id='skills_filter', n_clicks=0),
            width={"size": 2}
        ),
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label": x, "value": x}
                            for x in sorted(nurse_df["Area"].unique())
                        ]
                    ),
                ),
                id="area_filter_checklist",
                is_open=False,
            ),
            width={'size': 2, 'offset': 3}
        ),
        dbc.Col(
            dbc.Collapse(
                dbc.Card(
                    dcc.Checklist(
                        options=[
                            {"label": x, "value": x}
                            for x in sorted(nurse_df["Num_Patients"].unique())
                        ],
                    ),
                ),
                id="num_patients_checklist",
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
                        ]
                    ),
                ),
                id="skills_filter_checklist",
                is_open=False,
            ),
            width={'size': 2}
        ),

    ]),
    dbc.Row([
        dbc.ListGroup([
            # dbc.ListGroupItem(x) for x in nurse_info_list
            dbc.ListGroupItem(id='listed_nurse')
        ])
    ])
], fluid=True)]

content = html.Div(aa, id="page-content")

app.layout = dbc.Container([
    dcc.Location(id="url"),
    header,
    html.Br(),
    # sidebar,
    dbc.Row([
        dbc.Col([
            sidebar
        ], width={'size': 1}),
        dbc.Col([content], width={'size': 11}),
    ])
], fluid=True)


# callbacks
# dropdown_list
# @app.callback(
#     Output('listed_nurse', 'children'),
#     [Input('Name', 'value'),
#     Input('area_filter_checklist', 'value'),
#     Input('num_patients_checklist', 'value'),
#     Input('skills_filter_checklist', 'value')]
# )
# def filter_list(name_list, area_list, patients_list, skills_list):
#     valid_nurses = []
#     if(!(name_list)):


# basic
@app.callback(
    Output("area_filter_checklist", "is_open"),
    Input("area_filter", "n_clicks"),
    [State("area_filter_checklist", "is_open")],
)
def toggle_left(n_area_filter, is_open):
    if n_area_filter:
        return not is_open
    return is_open


@app.callback(
    Output("num_patients_checklist", "is_open"),
    Input("num_patients_filter", "n_clicks"),
    [State("num_patients_checklist", "is_open")],
)
def toggle_left(n_num_patients_filter, is_open):
    if n_num_patients_filter:
        return not is_open
    return is_open


@app.callback(
    Output("skills_filter_checklist", "is_open"),
    Input("skills_filter", "n_clicks"),
    [State("skills_filter_checklist", "is_open")],
)
def toggle_left(n_skills_filter, is_open):
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
