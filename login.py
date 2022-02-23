import dash_bootstrap_components as dbc
from dash import Input, Output, Dash
from dash import html

# Bootstrap package needs to download to run

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

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
            dbc.Input(id = "userid", type="email", placeholder="Enter email"),
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
                [dbc.NavItem(dbc.NavLink("Login", href="https://google.com", active=True)),
                 dbc.NavItem(dbc.NavLink("Forgot Username/Password", href="https://google.com", active=True)),
                 ], pills=True,),
            html.Div(id='output'),
        ])
    ])
])
@app.callback(Output("output", "children"),
            Input('userid', 'value'),
            Input('password', 'value')
)
def navigation(userid, password):
    return False

if __name__ == "__main__":
    app.run_server(debug=True)
