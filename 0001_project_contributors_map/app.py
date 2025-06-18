import streamlit as st
import yaml
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# Load YAML data
with open("contributors.yaml", "r") as file:
    data = yaml.safe_load(file)["contributors"]

# Convert to DataFrame
df = pd.DataFrame(data)

# Sidebar filters
st.sidebar.header("Filter Contributors")
roles = st.sidebar.multiselect("Role", df["role"].unique(), default=df["role"].unique())
countries = st.sidebar.multiselect("Country", df["country"].unique(), default=df["country"].unique())
employers = st.sidebar.multiselect("Employer", df["employer"].unique(), default=df["employer"].unique())
teams = st.sidebar.multiselect("Team", df["team"].unique(), default=df["team"].unique())

# Filter data
filtered_df = df[
    df["role"].isin(roles) &
    df["country"].isin(countries) &
    df["employer"].isin(employers) &
    df["team"].isin(teams)
]

# Team color map (Folium supports limited named colors)
team_colors = [
    "red", "blue", "green", "purple", "orange", "darkred", "lightred", "beige",
    "darkblue", "darkgreen", "cadetblue", "darkpurple", "white", "pink",
    "lightblue", "lightgreen", "gray", "black", "lightgray"
]
unique_teams = sorted(filtered_df["team"].unique())
color_map = {team: team_colors[i % len(team_colors)] for i, team in enumerate(unique_teams)}

# Map center
if not filtered_df.empty:
    map_center = [filtered_df["lat"].mean(), filtered_df["lon"].mean()]
    zoom_start = 3 if len(filtered_df) > 5 else 5
else:
    map_center = [20, 0]
    zoom_start = 2

# Create map and cluster
m = folium.Map(location=map_center, zoom_start=zoom_start)
marker_cluster = MarkerCluster().add_to(m)

# Add team-colored markers
for _, row in filtered_df.iterrows():
    popup = f"""
    <strong>{row['name']}</strong><br>
    Role: {row['role']}<br>
    Team: {row['team']}<br>
    Country: {row['country']}<br>
    Employer: {row['employer']}<br>
    GitHub: <a href='https://github.com/{row['github_id']}' target='_blank'>{row['github_id']}</a>
    """
    color = color_map.get(row["team"], "gray")
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=popup,
        tooltip=f"{row['name']} ({row['team']})",
        icon=folium.Icon(color=color, icon="user")
    ).add_to(marker_cluster)

# Add a simple legend with visible text
legend_html = """
<div style="position: fixed; bottom: 40px; left: 40px; width: 200px; height: auto;
    border:2px solid grey; z-index:9999; font-size:14px; background-color:white;
    color:black; padding:10px;">
    <b>Team Colors</b><br>
"""

for team, color in color_map.items():
    legend_html += f'<i style="background:{color};width:10px;height:10px;display:inline-block;margin-right:5px;"></i>{team}<br>'
legend_html += "</div>"
m.get_root().html.add_child(folium.Element(legend_html))

# Streamlit layout
st.title("🌍 Project Contributors Map")
st.markdown("Zoom and explore contributor data. Use sidebar to filter by role, country, employer, or team.")
st_folium(m, width=800, height=550)

# Interactive table
st.subheader("📋 Filtered Contributor Table")
st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)
