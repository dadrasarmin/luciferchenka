# Project Contributors Map
This is a simple interactive web application to visualize contributors of a project on a world map. Each contributor is displayed based on their geographic location and organizational affiliation, with filtering options for roles, employers, teams, and countries.

The app demonstrates:
1. Map-based visualization using Folium
2. Interactive filtering via Streamlit
3. Clustered markers with team-specific colors
4. A searchable, sortable table below the map

# How to Run
Install required packages (ideally in a virtual environment):
```
pip install streamlit pandas pyyaml folium streamlit-folium geopy
```
Start the Streamlit app:
```
streamlit run app.py
```
View in your browser (usually opens automatically at http://localhost:8501).
# Disclaimer
The contributor data in contributors.yaml is entirely synthetic and generated for demonstration purposes only. This code and dataset were generated with the help of ChatGPT (OpenAI) to assist with rapid prototyping.
# Videocast
[project_contributors_map.webm](https://github.com/user-attachments/assets/ea6eb6f6-d3ec-4b7f-9156-646188a0597a)
