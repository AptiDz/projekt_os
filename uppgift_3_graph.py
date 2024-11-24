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

sport_medals = df_gbr.groupby("Sport", observed=True)[["Medal"]].count() 
top_10_sports = sport_medals.sort_values(by="Medal", ascending=False).head(10)

fig = px.bar(
    top_10_sports,
    x=top_10_sports.index,
    y="Medal",
    labels={"x": "Sport", "Medal": "Number of Medals"},
    title="Number of Medals per Sport")

medals_sport = fig

# Graph Medals/GBR/OS

os_type_medals = df_gbr.groupby(['Games', 'Medal'], observed=True).size().unstack(fill_value=0) 

os_type_medals_index = os_type_medals.reset_index()

os_type_medals_melted = os_type_medals_index.melt(
id_vars=["Games"],
value_vars=["Bronze", "Silver", "Gold"],
var_name="Type of Medals",
value_name="Number of Type")

fig = px.bar(
os_type_medals_melted,
x="Games",
y="Number of Type",
color="Type of Medals",
title="Number of medals won by GBR on each OS",
labels={"Games": "Year", "Number of Type": "Number of Medals"},
color_discrete_map={"Bronze": "tan", "Silver": "silver", "Gold": "gold"})

fig.update_layout(
xaxis_tickangle=90,
barmode="stack")

medals_gbr_os = fig


