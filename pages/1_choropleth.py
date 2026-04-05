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
      
        df.columns = df.columns.str.strip()
        
       
        if 'state_code' in df.columns:
            df['state_code'] = df['state_code'].astype(str).str.zfill(2)
            
        return df
    except FileNotFoundError:
        st.error("Error: CSV file not found")
        return None

@st.cache_data
def load_geojson():
    try:
        with open('data/shapefiles/mexico_states.geojson', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Error: GeoJSON file not found")
        return None

df = load_data()
geojson = load_geojson()

if df is None or geojson is None:
    st.stop()


first_props = geojson['features'][0]['properties']
geo_key = 'CVE_ENT'
if 'CVEGEO' in first_props:
    geo_key = 'CVEGEO'
elif 'cve_ent' in first_props:
    geo_key = 'cve_ent'

feature_id_string = f"properties.{geo_key}"

st.subheader("Map")
st.write(f"Average FRI Score: {df['fri_score'].mean():.2f}")


hover_cols = ['state_name', 'supply_score', 'demand_score', 'digital_score', 'barriers_score']
available_cols = [col for col in hover_cols if col in df.columns]
customdata = df[available_cols].values


hovertemplate = '<b>%{customdata[0]}</b><br>FRI Score: %{z:.1f}<br>'
if len(available_cols) > 1: hovertemplate += 'Supply: %{customdata[1]:.1f}<br>'
if len(available_cols) > 2: hovertemplate += 'Demand: %{customdata[2]:.1f}<br>'
if len(available_cols) > 3: hovertemplate += 'Digital: %{customdata[3]:.1f}<br>'
if len(available_cols) > 4: hovertemplate += 'Barriers: %{customdata[4]:.1f}'
hovertemplate += '<extra></extra>'

st.subheader("Map Options")
# Create a dropdown menu
metric_choice = st.selectbox(
    "Select a metric to visualize on the map:",
    options=['fri_score', 'supply_score', 'demand_score', 'digital_score', 'barriers_score'],
    # This formats the ugly column names into clean text for the user
    format_func=lambda x: x.replace('_score', '').title().replace('Fri', 'Total FRI')
)

fig = go.Figure(data=go.Choroplethmapbox(
    z=df[metric_choice],
    locations=df['state_code'],
    geojson=geojson,
    featureidkey=feature_id_string,  
    colorscale='RdYlGn',
    zmin=0,
    zmax=100,
    colorbar=dict(title="FRI Score", thickness=15, len=0.7),
    hovertemplate=hovertemplate,
    customdata=customdata
))

fig.update_layout(
    mapbox=dict(style='carto-positron', zoom=3.5, center=dict(lat=23.6345, lon=-102.5528)),
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    height=600
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("State Scores")
st.dataframe(
    df[available_cols + ['fri_score']].sort_values('fri_score', ascending=False),
    use_container_width=True,
    hide_index=True  
)
