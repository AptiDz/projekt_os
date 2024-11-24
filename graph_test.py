import plotly.express as px
import pandas as pd
import hashlib as hl

anon_df = pd.read_csv("athlete_events.csv")
anon_df["Name"] = anon_df["Name"].apply(lambda name: hl.sha256(name.encode()).hexdigest())

def sport_age_people(sports):
    sport = anon_df[anon_df["Sport"] == sports].reset_index(drop=True)
    sport = sport.groupby(["Age"]).size().reset_index(name="Age Count")
    fig = px.bar(sport, x="Age", y="Age Count", color="Age", title="Number of individiuals with specific age for " + sports, labels={"Age Count": "Number of athletes"})
    
    return fig.show()
  
sport_age_boxing = sport_age_people("Boxing")