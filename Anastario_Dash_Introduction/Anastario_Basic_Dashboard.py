from dash import html, dcc, Dash, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

#data processing
df = pd.read_csv('NYC_Bicycle_Counts_2016_Corrected.csv')
df['Brooklyn Bridge'] = df['Brooklyn Bridge'].str.replace(',','').astype(float)
df['Manhattan Bridge'] = df['Manhattan Bridge'].str.replace(',','').astype(float)
df['Williamsburg Bridge'] = df['Williamsburg Bridge'].str.replace(',','').astype(float)
df['Queensboro Bridge'] = df['Queensboro Bridge'].str.replace(',','').astype(float)
df['Total'] = df['Total'].str.replace(',','').astype(float)

#app layout
app.layout = html.Div([
    dcc.Dropdown(id = 'bridge',
                options=[
                    {"label": "Brooklyn Bridge", "value": "Brooklyn Bridge"},
                    {"label": "Manhattan Bridge", "value": "Manhattan Bridge"},
                    {"label": "Williamsburg Bridge", "value": "Williamsburg Bridge"},
                    {"label": "Queensboro Bridge", "value": "Queensboro Bridge"}],
                multi = False,
                value = 'Brooklyn Bridge',
                style={'width': "40%"}
                ),
    html.Div(id = 'Output Container'),
    html.Br(),
    dcc.Graph(id='bridge_bar', figure={})
])

#callback
@app.callback(
    [Output('Output Container', 'children'),
    Output('bridge_bar', 'figure')],
    Input('bridge', 'value'),
)
def update_graph(bridge):
    container = "Bridge Selected: {}".format(bridge)
    fig ={
        'data':[
             {'y': df[bridge], 'x': df['Day'], 'type': 'bar', 'name': bridge},
        ],
        'layout':{
            'title':'This is a Test Dashboard with Old Bycicle Data'
        }
    }

    return container, fig




if __name__ == '__main__':
    app.run_server(debug = True)