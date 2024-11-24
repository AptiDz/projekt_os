import plotly.express as px
import pandas as pd
import hashlib as hl

# Variabels for graphs

anon_df = pd.read_csv("athlete_events.csv")
anon_df["Name"] = anon_df["Name"].apply(lambda name: hl.sha256(name.encode()).hexdigest())

df_gbr = anon_df[anon_df["NOC"] == "GBR"]

sport_medals = df_gbr.groupby("Sport", observed=True)[["Medal"]].count() 
top_10_sports = sport_medals.sort_values(by="Medal", ascending=False).head(10)

medals = anon_df[anon_df["Medal"].notna()].reset_index(drop=True)


# Graph Medals/Sport

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

# Graph Paticipants/Ages 

fig = px.histogram( 
    df_gbr,
    x="Age",
    nbins=8,
    title="OS-GBR: Participants Ages",
    labels={"Age": "Age Bracket", "Count" : "Number of Individuals"})

fig.update_layout(yaxis_title="Number of Individuals")

participants_ages = fig

# Graph Medals/Football/Countries

def sport_medals(sports):
    
    sport = medals[medals["Sport"] == sports].reset_index(drop=True)
    sport = sport.groupby(["NOC", "Medal"]).size().reset_index(name="Medal Count")

    fig = px.bar(sport, x="NOC", y="Medal Count", color="Medal", color_discrete_map = {"Bronze": "tan", "Silver": "silver", "Gold": "gold"}, title="Countries with number of medals for " + sports, labels={"NOC": "Country", "Medal Count": "Number of Medals"})

    return fig

sport_medals_football = sport_medals("Football")

# Graph Medals/Swimming/Countries

sport_medals_swimming = sport_medals("Swimming")

# Graph Medals/Boxing/Countries

sport_medals_boxing = sport_medals("Boxing")

# Graph Medals/Rugby/Countries

sport_medals_rugby = sport_medals("Rugby")


# Graph Idividuals/Age/Football

def sport_age_people(sports):
    sport = anon_df[anon_df["Sport"] == sports].reset_index(drop=True)
    sport = sport.groupby(["Age"]).size().reset_index(name="Age Count")
    fig = px.bar(sport, x="Age", y="Age Count", color="Age", title="Number of individiuals with specific age for " + sports, labels={"Age Count": "Number of athletes"})
    
    return fig
  
sport_age_football = sport_age_people("Football")


# Graph Idividuals/Age/Swimming

sport_age_swimming = sport_age_people("Swimming")

# Graph Idividuals/Age/Boxing

sport_age_boxing = sport_age_people("Boxing")
