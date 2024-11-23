from dash import Dash, html, Output, Input, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import hashlib as hl
import plotly_express as px


app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])

button = html.Div(
    [
        dbc.Button(
            "Click me", id="example-button", className="me-2", n_clicks=0
        ),
        html.Span(id="example-output", style={"verticalAlign": "middle"}),
    ]
)


@app.callback(
    Output("example-output", "children"), [Input("example-button", "n_clicks")]
)
def on_button_click(n):
    if n is None:
        return "Not clicked."
    else:
        return f"Clicked {n} times."

app.layout = html.Div([
   html.H1(
            "Welcome to our Dashboard!",
        ) , button, 
   html.Div(dcc.Graph(id="graph"))
])

if __name__ == "__main__":
    app.run(debug=True)
    

    
    
"""
Källförteckning

https://github.com/pr0fez/AI24-Databehandling 
https://dashcheatsheet.pythonanywhere.com/
https://dash-bootstrap-components.opensource.faculty.ai

"""