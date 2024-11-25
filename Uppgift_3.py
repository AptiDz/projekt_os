import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from uppgift_3_graph import *

# Intializes dash in its darkly theme
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Server to get it running in render
server = app.server

# Defines the layout
app.layout = html.Div(
    [html.H1(
            "Great Britain in OS!", className="mb-5",
        ),
        dbc.Button("Medals/Sport", id="button1", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Medals/GBR/OS", id="button2", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Participants/Ages", id="button3", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Medals/Football/Countries", id="button4", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Medals/Swimming/Countries", id="button5", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Medals/Boxing/Countries", id="button6", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Medals/Rugby/Countries", id="button7", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Individuals/Age/Football", id="button8", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Individuals/Age/Swimming", id="button9", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Individuals/Age/Boxing", id="button10", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Individuals/Age/Rugby", id="button11", className="me-2 mb-5", n_clicks=0),
        html.Div(
            dcc.Graph(id="graph")  # The graph updates dynamically
        ),
    ], className="m-5" # m is margin where each number represants 16 pixels
)

# Defining the callbacks
@app.callback(
    Output("graph", "figure"),  # Targets "figure" property of the graph
    [Input(f"button{i+1}", "n_clicks") for i in range(11)]
)
def interact_graph(*btns):
    # Determining which button was based on clicks on n_clicks
    ctx = dash.callback_context
    if not ctx.triggered:
        return {}  # Returns the empty figure by default
    # id = ctx.triggered returns id.n_clicks (index[0] = id, index[1] = n_clicks)
    id = ctx.triggered[0]["prop_id"].split(".")[0] 

    # id checks the condition of of dbc.button id
    if id == "button1":
        return medals_sport

    elif id == "button2":
        return medals_gbr_os
        
    elif id == "button3":
        return participants_ages

    elif id == "button4":
        return sport_medals("Football")
    
    elif id == "button5":
        return sport_medals("Swimming")
    
    elif id == "button6":
        return sport_medals("Boxing")
    
    elif id == "button7":
        return sport_medals("Rugby")
    
    elif id == "button8":
        return sport_age_people("Football")

    elif id == "button9":
        return sport_age_people("Swimming")

    elif id == "button10":
        return sport_age_people("Boxing")

    elif id == "button11":
        return sport_age_people("Rugby")
    
    else:
        return {}  # At the start of the dash without clicking button results empty figure

# Runs the dash
if __name__ == "__main__":
    app.run_server(debug=True)
    
    
"""
Källförteckning

https://github.com/pr0fez/AI24-Databehandling 
https://dashcheatsheet.pythonanywhere.com/
https://dash-bootstrap-components.opensource.faculty.ai

"""