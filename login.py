import dash_bootstrap_components as dbc
import pandas as pd
from dash import Input, Output, Dash, State
from dash import html

# Bootstrap package needs to download to run

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

sampleData = {
    "a": "a",
    "b": "b",
    "c": "c",
}

app.layout = dbc.Container([
    # Title
    dbc.Row([
        dbc.Col(html.H1("Nurse Dashboard Log In", className='text-center'),
                width=12),
    ]),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    # First Row - Username input box
    dbc.Row([
        dbc.Col([]),
        dbc.Col([
            dbc.Label("Username", html_for="example-email"),
            dbc.Input(id = "userid", placeholder="Enter email"),
            dbc.FormText(
                "Enter your username",
                color="secondary", ),
        ]),
    ]),

    # Second Row - password input box
    dbc.Row([
        dbc.Col([]),
        dbc.Col([
            dbc.Label("Password", html_for="password-a"),
            dbc.Input(id = "password", type="password", placeholder="Enter password"),
            dbc.FormText(
                "Enter your password",
                color="secondary", ),
        ])
    ]),

    # Third Row - Log In Button & Forgot username/password
    dbc.Row([
        dbc.Col([]),
        dbc.Col([
            dbc.Nav(
                [dbc.NavItem(dbc.NavLink("Login", id = "login-button",href="https://google.com", active=True)),
                 dbc.NavItem(dbc.NavLink("Forgot Username/Password", href="https://google.com", active=True)),
                 ], pills=True,),
            html.Div(id='output'),
        ])
    ])
])
@app.callback(Output("output", "children"),
            Input('userid', 'value'),
            Input('password', 'value'),
            Input('login-button', 'n_clicks'),
)
def navigation(userid, password,n_clicks):
    if n_clicks == None:
        print("nothing yet")
    elif int(n_clicks) >= 1:
        if userid in sampleData.keys():
            if password == sampleData[userid]:
                print("success")
        else:
            print("failed")
    else:
        print("notihign yet")



if __name__ == "__main__":
    app.run_server(debug=True)
