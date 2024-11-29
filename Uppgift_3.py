# Imports the libraries.
# Imports libraries, variables and functions from the file.
from dash import Dash, html, dcc, Input, Output, ctx
import dash_bootstrap_components as dbc
from uppgift_3_graph import *

# Intializes dash in its darkly theme
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Server to get it running in render online
server = app.server

# Defines the layout
app.layout = html.Div(
    [html.H1(
            "Great Britain in OS!", className="mb-5",
        ) # Creates the title for the dash app and its gets margin by 5 on bottom so the buttons have distance verticly
        ,
        
        # Title for upper 3 buttons which represants Country statistics
        html.H3("Country Statistics", className="mb-3"), 
        
        # Creates the buttons with specific name and id and margin me means margin ends with has distance to next element on the right side. n_clicks represents that the button is not clicked at the start.
        dbc.Button("Medals/Sport", id="button1", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Medals/GBR/OS", id="button2", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Participants/Ages", id="button3", className="me-2 mb-5", n_clicks=0),
        
         # Title for the lower 8 buttons which represants Sport statistics
        html.H3("Sport Statistic", className="mb-3"),  # Subheading with bottom margin
        
        dbc.Button("Medals/Football/Countries", id="button4", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Medals/Swimming/Countries", id="button5", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Medals/Boxing/Countries", id="button6", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Medals/Rugby/Countries", id="button7", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Individuals/Age/Football", id="button8", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Individuals/Age/Swimming", id="button9", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Individuals/Age/Boxing", id="button10", className="me-2 mb-5", n_clicks=0),
        dbc.Button("Individuals/Age/Rugby", id="button11", className="me-2 mb-5", n_clicks=0), 
        # Bottom margin to separate from next section,
        html.Div(
            dcc.Graph(id="graph")  # The graph updates dynamically
        ),
    ], className="m-5" # m is margin where each number represants 16 pixels
)

# Defining the callbacks
@app.callback(
    Output("graph", "figure"),  # Targets "figure" property of the graph as the output
    [Input(f"button{i+1}", "n_clicks") for i in range(11)] # Input uppdates n_clicks by pressing the specific button.
)
def interact_graph(*btns):
    # Determining which button was based on clicks on n_clicks
    if not ctx.triggered:
        return {}  # Returns the empty figure by default
    # id = ctx.triggered returns id.n_clicks (index[0] = id, index[1] = n_clicks). Second [0] returns the first element this case button"(n)"
    id = ctx.triggered[0]["prop_id"].split(".")[0] 
    # id checks the condition of of dbc.button id and returns the specific values in this case the variables that plots the plotly
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

# Runs the dash with debug features on which provides detailed error messages.
if __name__ == "__main__":
    app.run_server(debug=True)
    
    
"""
Källförteckning

https://github.com/pr0fez/AI24-Databehandling 
https://dashcheatsheet.pythonanywhere.com/
https://dash-bootstrap-components.opensource.faculty.ai/docs/components/button/
https://dash.plotly.com/advanced-callbacks


"""