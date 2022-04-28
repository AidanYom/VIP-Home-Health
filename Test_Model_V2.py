from logging import PlaceHolder
from dash import html, dcc, Dash, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import dash_auth
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


'''
The folowing block of code reads from the firestore database and puts the code into a pandas dataframe. 
Note: this will only work if you download the fir-practice-17c... code into the folder that this code is in.
The dataframe is printed at the end for clarity, that is not essential to the function of the code.
'''
if not firebase_admin._apps:
    cred = credentials.Certificate(r'fir-practice-17cce-firebase-adminsdk-ygbmg-0bde5e4b86.json') 
    default_app = firebase_admin.initialize_app(cred)

db = firestore.client()
patients = list(db.collection(u'Patients').stream())
patients_dict = list(map(lambda x: x.to_dict(), patients))
df = pd.DataFrame(patients_dict)
print(df)
# make sample data to read from

'''
The following block (lines 30 - 52) create dataframes for the patient and the nurse list. 
This data is not read from the firestore database, that is something that needs to be done.
'''
nurse_data = {'Name': ['Jack Knox', 'Hanna Ertel', 'Aidan Anastario', 'Kaushik Karthik', 'Miranda Chai', 'Jay Kee'],
              'Area': ['Lafayette', 'Staten Island', 'Bronx', 'Manhattan', 'Queens', 'Brooklyn'],
              'Num_Patients': [5, 4, 7, 5, 3, 6],
              'Hospice': [0, 0, 1, 0, 1, 1],
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

'''
The following block (56-93) puts a task list, nurse list, and patient list into list form.
The task list is just a filler for the main dashboard page. Hopefully the tasks can be read
from input and appeneded to the list, but we did not incorporate that yet.
The nurse and patient df are read, and inputted into a list of lists, where each list a different
patient/nurse, and all of their information is in the nested list.
'''
task_list = ["test basic task\n", "this task is hard\n"]

for x in range(0, len(nurse_df)):
    nurse_info_list.append([])
    nurse_info_list[x].append(nurse_df.at[x, 'Name'])
    nurse_info_list[x].append(nurse_df.at[x, 'Area'])
    nurse_info_list[x].append(str(nurse_df.at[x, 'Num_Patients']))
    if (nurse_df.at[x, 'Hospice'] == 1):
        nurse_info_list[x].append("Hospice")
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

'''
Here is where we set the theme to the basic bootstrap theme. This can be changed here.
This is also where you can adjust the settings to allow for a mobile compenent.
'''
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# add a mobile layout component later

'''
Implements a user authentication feature. 
This does not read data from the database. Use the given ID and password to get into the webpage. 
'''
auth = dash_auth.BasicAuth(
    app,
    {'ID': 'password',
     'ID2': 'password2'}
)

'''
This is shown when there is an error loading a page.
'''
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

'''
This is the sidebar. There are buttons on the left side of the dashboard
that let users navigate the site, and this sets that up.
'''
sidebar = html.Div([
    dbc.Nav([
        dbc.NavLink("Home", href="/", active="exact"),
        dbc.NavLink("Nurses", href="/nurse_dash", active="exact"),
        dbc.NavLink("Patients", href="/patient_dash", active="exact"),
        dbc.NavLink("Setting", href="/settings", active="exact"),
    ],
        vertical=True,
        pills=True,
    )
])

'''
This is the nurse page header. Just what is says at the top of the page.
'''
nurse_header = dbc.Container([
    dbc.Row([
        html.H1("Nurse Dashboard", className="text-center text-secondary"),
    ])
])

'''
This is the patient page header. Just what is says at the top of the page.
'''
patient_header = dbc.Container([
    dbc.Row([
        html.H1("Patient Dashboard", className="text-center text-secondary"),
    ])
])

'''
This is the main page header. Just what is says at the top of the page.
'''
main_header = dbc.Container([
    dbc.Row([
        html.H1("Dashboard", className="text-center text-secondary"),
    ])
])

'''
This models the layout of the main page. Still needs a lot of work. We need to 
incorporate a calendar, dynamic task list, make the edit data buttons work, and add
any other things that will be relevant.
'''
main_dash_page = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Calendar"),
                dbc.CardBody(html.H5("this will show a snapshot of the calendar"))
            ])
        ], width = {'size':8}),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.H5("Data Entry")
                ], width={"offset": 4, 'size':6})
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("New Patient Entry")
                    ]),
                    #html.Br(),
                    dbc.Card([
                        dbc.CardHeader("Edit Patient Data")
                    ])
                ], width = {'offset':0, 'size':6}),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("New Nurse Entry")
                    ]),
                    #html.Br(),
                    dbc.Card([
                        dbc.CardHeader("Edit Nurse Data")
                    ])
                ], width ={'offset':0,'size':6}),
            ])
        ])

    ]),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Card([
                    dbc.CardHeader("Nurse List Preview"),
                    dbc.CardBody(
                        dbc.ListGroup([
                            dbc.ListGroupItem(dbc.Row(
                                (dbc.Col(x[0], width={'size':6}),
                                dbc.Col(x[1], width={'size':4})),
                                className='gx-5'
                            )) for x in nurse_info_list
                        ])
                    )
                ])
            ])
        ], width={"size": 4}),
        dbc.Col([
            dbc.Row(
                html.P("talk to data team about data entry")
            ),
            dbc.Row(
                dcc.Checklist(task_list, inline=False)
            )
        ])
    ])
])

'''
This is the nurse page. Fairly self-explanatory if you understand Dash.
'''
nurse_dash_page = [dbc.Container([
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
            dbc.Button("Expertise", outline=True, id='skills_filter', n_clicks=0),
            width={"size": 3},
            align='start'
        ),
        dbc.Col([
            dcc.Dropdown(
                id="sort_by",
                options=[
                    {"label":"Area (default)", "value":"Area (default)"},
                    {"label":"Alphabetical", "value":"Alphabetical"},
                    {"label":"# Patients (low to high)", "value":"# Patients (low to high)"},
                    {"label":"# Patients (high to low)", "value":"# Patients (high to low)"},
                ],
                multi=False,
                placeholder="Sort by"
            ),
        ], width={"size":2}),
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
                            {"label": "Hospice", "value": "Hospice"},
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

'''
This is the patient page. Fairly self-explanatory if you understand Dash.
'''
patient_page_dash = [dbc.Container([
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
            width={"size": 3},
            align='start'
        ),
        dbc.Col([
            dcc.Dropdown(
                id="patient_sort_by",
                options=[
                    {"label":"Area (default)", "value":"Area (default)"},
                    {"label":"Alphabetical (Patient)", "value":"Alphabetical (Patient)"},
                    {"label": "Alphabetical (Nurse)", "value": "Alphabetical (Nurse)"},
                ],
                multi=False,
                placeholder="Sort by"
            ),
        ], width={"size":2}),
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
                id="assigned_nurse_collapse",
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
                        id="sd_filter_checklist"
                    ),
                ),
                id="sd_collapse",
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

content = html.Div(id="page-content")

header = html.Div(id="page-header")

'''
This is the app.layout, or what is going to be displayed.
'''
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

# callbacks
@app.callback(
    Output('nurse_group_list', 'children'),
    [Input('Name', 'value'),
     Input('area_filter_checklist', 'value'),
     Input('num_patients_checklist', 'value'),
     Input('skills_filter_checklist', 'value'),
     Input('sort_by', 'value')]
)
def nurse_filter_list(name_list, area_list, num_patients_list, skills_list, sort_by):
    filtered_list = []
    unsorted_list = []
    sorted_list = []
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
            unsorted_list.append(x)

    if (sort_by == "Alphabetical"):
        for x in range(len(unsorted_list)):
            idx = 0
            while (idx < len(sorted_list)):
                letter_idx = 0
                while (letter_idx < len(sorted_list[idx][0]) - 1 and letter_idx < len(unsorted_list[x][0]) - 1 and
                       sorted_list[idx][0][letter_idx] == unsorted_list[x][0][letter_idx]):
                    letter_idx += 1
                if (ord(sorted_list[idx][0][letter_idx]) > ord(unsorted_list[x][0][letter_idx])):
                    break
                else:
                    idx += 1
            sorted_list.insert(idx, unsorted_list[x])
    elif (sort_by == "# Patients (low to high)"):
        for x in range(len(unsorted_list)):
            idx = 0
            while (idx < len(sorted_list)):
                letter_idx = 0
                while (letter_idx < len(sorted_list[idx][2]) - 1 and letter_idx < len(unsorted_list[x][2]) - 1 and
                       sorted_list[idx][2][letter_idx] == unsorted_list[x][2][letter_idx]):
                    letter_idx += 1
                if (sorted_list[idx][2] == unsorted_list[x][2]):
                    letter_idx = 0
                    while (letter_idx < len(sorted_list[idx][0]) - 1 and letter_idx < len(unsorted_list[x][0]) - 1 and
                           sorted_list[idx][0][letter_idx] == unsorted_list[x][0][letter_idx]):
                        letter_idx += 1
                    if (ord(sorted_list[idx][0][letter_idx]) > ord(unsorted_list[x][0][letter_idx])):
                        break
                    else:
                        idx += 1
                else:
                    if (ord(sorted_list[idx][2][letter_idx]) > ord(unsorted_list[x][2][letter_idx])):
                        break
                    else:
                        idx += 1
            sorted_list.insert(idx, unsorted_list[x])
    elif (sort_by == "# Patients (high to low)"):
        for x in range(len(unsorted_list)):
            idx = 0
            while (idx < len(sorted_list)):
                letter_idx = 0
                while (letter_idx < len(sorted_list[idx][2]) - 1 and letter_idx < len(unsorted_list[x][2]) - 1 and
                       sorted_list[idx][2][letter_idx] == unsorted_list[x][2][letter_idx]):
                    letter_idx += 1
                if (sorted_list[idx][2] == unsorted_list[x][2]):
                    letter_idx = 0
                    while (letter_idx < len(sorted_list[idx][0]) - 1 and letter_idx < len(unsorted_list[x][0]) - 1 and
                           sorted_list[idx][0][letter_idx] == unsorted_list[x][0][letter_idx]):
                        letter_idx += 1
                    if (ord(sorted_list[idx][0][letter_idx]) > ord(unsorted_list[x][0][letter_idx])):
                        break
                    else:
                        idx += 1
                else:
                    if (ord(sorted_list[idx][2][letter_idx]) < ord(unsorted_list[x][2][letter_idx])):
                        break
                    else:
                        idx += 1
            sorted_list.insert(idx, unsorted_list[x])
    elif (sort_by == "Area (default)" or True):
        for x in range(len(unsorted_list)):
            idx = 0
            while (idx < len(sorted_list)):
                letter_idx = 0
                while (letter_idx < len(sorted_list[idx][1]) - 1 and letter_idx < len(unsorted_list[x][1]) - 1 and
                       sorted_list[idx][1][letter_idx] == unsorted_list[x][1][letter_idx]):
                    letter_idx += 1
                if (sorted_list[idx][1] == unsorted_list[x][1]):
                    letter_idx = 0
                    while (letter_idx < len(sorted_list[idx][0]) - 1 and letter_idx < len(unsorted_list[x][0]) - 1 and
                           sorted_list[idx][0][letter_idx] == unsorted_list[x][0][letter_idx]):
                        letter_idx += 1
                    if (ord(sorted_list[idx][0][letter_idx]) > ord(unsorted_list[x][0][letter_idx])):
                        break
                    else:
                        idx += 1
                else:
                    if (ord(sorted_list[idx][1][letter_idx]) > ord(unsorted_list[x][1][letter_idx])):
                        break
                    else:
                        idx += 1
            sorted_list.insert(idx, unsorted_list[x])

    for x in sorted_list:
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
     Input('sd_filter_checklist', 'value'),
     Input('patient_sort_by', 'value')]
)
def patient_filter_list(name_list, area_list, num_patients_list, skills_list, patient_sort_by):
    filtered_list = []
    unsorted_list = []
    sorted_list = []
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
            unsorted_list.append(x)

    if (patient_sort_by == "Alphabetical (Patient)"):
        for x in range(len(unsorted_list)):
            idx = 0
            while (idx < len(sorted_list)):
                letter_idx = 0
                while (letter_idx < len(sorted_list[idx][0]) - 1 and letter_idx < len(unsorted_list[x][0]) - 1 and
                       sorted_list[idx][0][letter_idx] == unsorted_list[x][0][letter_idx]):
                    letter_idx += 1
                if (ord(sorted_list[idx][0][letter_idx]) > ord(unsorted_list[x][0][letter_idx])):
                    break
                else:
                    idx += 1
            sorted_list.insert(idx, unsorted_list[x])
    
    elif (patient_sort_by == "Alphabetical (Nurse)"):
        for x in range(len(unsorted_list)):
            idx = 0
            while (idx < len(sorted_list)):
                letter_idx = 0
                while (letter_idx < len(sorted_list[idx][2]) - 1 and letter_idx < len(unsorted_list[x][2]) - 1 and
                       sorted_list[idx][2][letter_idx] == unsorted_list[x][2][letter_idx]):
                    letter_idx += 1
                if (ord(sorted_list[idx][2][letter_idx]) > ord(unsorted_list[x][2][letter_idx])):
                    break
                else:
                    idx += 1
            sorted_list.insert(idx, unsorted_list[x])

    elif (patient_sort_by == "Area (default)" or True):
        for x in range(len(unsorted_list)):
            idx = 0
            while (idx < len(sorted_list)):
                letter_idx = 0
                while (letter_idx < len(sorted_list[idx][1]) - 1 and letter_idx < len(unsorted_list[x][1]) - 1 and
                       sorted_list[idx][1][letter_idx] == unsorted_list[x][1][letter_idx]):
                    letter_idx += 1
                if (sorted_list[idx][1] == unsorted_list[x][1]):
                    letter_idx = 0
                    while (letter_idx < len(sorted_list[idx][0]) - 1 and letter_idx < len(unsorted_list[x][0]) - 1 and
                           sorted_list[idx][0][letter_idx] == unsorted_list[x][0][letter_idx]):
                        letter_idx += 1
                    if (ord(sorted_list[idx][0][letter_idx]) > ord(unsorted_list[x][0][letter_idx])):
                        break
                    else:
                        idx += 1
                else:
                    if (ord(sorted_list[idx][1][letter_idx]) > ord(unsorted_list[x][1][letter_idx])):
                        break
                    else:
                        idx += 1
            sorted_list.insert(idx, unsorted_list[x])
    
    for x in sorted_list:
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
    Output("page-header", "children"),
    Input("url", "pathname")
)
def render_page(pathname):
    if pathname == "/":
        return main_dash_page, main_header
    elif pathname == "/nurse_dash":
        return nurse_dash_page, nurse_header
    elif pathname == "/patient_dash":
        return patient_page_dash, patient_header
    elif pathname == "/settings":
        return [
            html.H5("Settings")
        ]
    return [jumbotron]

if __name__ == '__main__':
    app.run_server(debug=False)
