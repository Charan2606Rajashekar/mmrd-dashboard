import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json

st.title("Fintech Readiness Map")
st.write("Geographic visualization of FRI scores across Mexican states")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/processed/state_summary_with_fri.csv')
        return df
    except FileNotFoundError:
        st.error("Error: CSV file not found")
        return None

@st.cache_data
def load_geojson():
    try:
        with open('data/shapefiles/mexico_states.geojson', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Error: GeoJSON file not found")
        return None

df = load_data()
geojson = load_geojson()

if df is None or geojson is None:
    st.stop()

st.subheader("Map")
st.write(f"Average FRI Score: {df['fri_score'].mean():.2f}")

fig = go.Figure(data=go.Choroplethmapbox(
    z=df['fri_score'],
    locations=df['state_code'],
    geojson=geojson,
    featureidkey="properties.CVE_ENT",  
    colorscale='RdYlGn',
    zmin=0,
    zmax=100,
    colorbar=dict(title="FRI Score", thickness=15, len=0.7),
    # Simplified hover template below:
    hovertemplate='<b>%{customdata[0]}</b><br>FRI Score: %{z:.1f}<extra></extra>',
    customdata=df[['state_name']].values
))

fig.update_layout(
    mapbox=dict(style='carto-positron', zoom=3.5, center=dict(lat=23.6345, lon=-102.5528)),
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    height=600
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("State Scores")
st.dataframe(df[['state_name', 'fri_score', 'supply_score', 'demand_score', 'digital_score', 'barriers_score']].sort_values('fri_score', ascending=False))
