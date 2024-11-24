import plotly.express as px
import pandas as pd
import hashlib as hl

anon_df = pd.read_csv("athlete_events.csv")
anon_df["Name"] = anon_df["Name"].apply(lambda name: hl.sha256(name.encode()).hexdigest())



df_gbr = anon_df[anon_df["NOC"] == "GBR"]

fig = px.histogram(
    df_gbr,
    x="Age",
    nbins=8,
    title="OS-GBR: Participants Ages",
    labels={"Age": "Age Bracket", "Count" : "Number of Individuals"})

fig.update_layout(yaxis_title="Number of Individuals")

fig.show()