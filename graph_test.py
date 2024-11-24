import plotly.express as px
import pandas as pd
import hashlib as hl

anon_df = pd.read_csv("athlete_events.csv")
anon_df["Name"] = anon_df["Name"].apply(lambda name: hl.sha256(name.encode()).hexdigest())


sport_medals = anon_df.groupby("Sport", observed=True)[["Medal"]].count() 
top_10_sports = sport_medals.sort_values(by="Medal", ascending=False).head(10)

fig = px.bar(
        top_10_sports,
        x=top_10_sports.index,
        y="Medal",
        labels={"x": "Sport", "Medal": "Number of Medals"},
        title="Number of Medals per Sport")

fig.show()