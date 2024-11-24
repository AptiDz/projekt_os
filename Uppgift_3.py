import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from uppgift_3_graph import *

# Intializes dash in its darkly theme
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

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
     Input("button1", "n_clicks"),
    [Input("button2", "n_clicks"),
     Input("button3", "n_clicks"),
     Input("button4", "n_clicks"),
     Input("button5", "n_clicks"),
     Input("button6", "n_clicks"),
     Input("button7", "n_clicks"),
     Input("button8", "n_clicks"),
     Input("button9", "n_clicks"),
     Input("button10", "n_clicks"),
     Input("button11", "n_clicks")]
)
def interact_graph(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11):
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
        return sport_medals_football
    
    elif id == "button5":
        return sport_medals_swimming
    
    elif id == "button6":
        return sport_medals_boxing
    
    elif id == "button7":
        return sport_medals_rugby
    
    elif id == "button8":
        return sport_age_football

    elif id == "button9":
        return sport_age_swimming

    elif id == "button10":
        return sport_age_boxing

    elif id == "button11":
        return sport_age_rugby
    
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