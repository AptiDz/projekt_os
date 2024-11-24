import plotly.express as px
import pandas as pd
import hashlib as hl


anon_df = pd.read_csv("athlete_events.csv")
anon_df["Name"] = anon_df["Name"].apply(lambda name: hl.sha256(name.encode()).hexdigest())

df_gbr = anon_df[anon_df["NOC"] == "GBR"]

sport_medals = df_gbr.groupby("Sport", observed=True)[["Medal"]].count() 
top_10_sports = sport_medals.sort_values(by="Medal", ascending=False).head(10)

medals = anon_df[anon_df["Medal"].notna()].reset_index(drop=True)


# Graph Medals/Sport

def sport_medals(sports):
    
    sport = medals[medals["Sport"] == sports].reset_index(drop=True)
    sport = sport.groupby(["NOC", "Medal"]).size().reset_index(name="Medal Count")

    fig = px.bar(sport, x="NOC", y="Medal Count", color="Medal", color_discrete_map = {"Bronze": "tan", "Silver": "silver", "Gold": "gold"}, title="Countries with number of medals for " + sports, labels={"NOC": "Country", "Medal Count": "Number of Medals"})

    return fig

sport_medals_football = sport_medals("Football")