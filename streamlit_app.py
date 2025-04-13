import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('Tourism Dataset Lebanon 2023.csv')

#data cleaning: 
df.replace('https://dbpedia.org/page/Mount_Lebanon_Governorate', ' Mount Lebanon', inplace=True)
df.replace('https://dbpedia.org/page/South_Governorate', ' South Lebanon', inplace=True)
df.replace('https://dbpedia.org/page/Akkar_Governorate', 'Akkar', inplace= True)
df.replace('https://dbpedia.org/page/North_Governorate', 'North Lebanon', inplace= True)
df.replace('http://dbpedia.org/resource/Baabda_District', 'Baabda', inplace=True)
df.replace('http://dbpedia.org/resource/Byblos_District', 'Byblos', inplace=True)
df.replace('https://dbpedia.org/page/Nabatieh_Governorate','Nabatieh', inplace=True)
df.replace('http://dbpedia.org/resource/Tyre_District', 'Tyre', inplace=True)
df.replace('http://dbpedia.org/resource/Bsharri_District', 'Bsharri', inplace=True)
df.replace('http://dbpedia.org/resource/Sidon_District', 'Sidon', inplace =True)
df.replace('http://dbpedia.org/resource/Batroun_District', 'Batroun', inplace=True)
df.replace('http://dbpedia.org/resource/Zgharta_District','Zgharta', inplace=True)
df.replace('http://dbpedia.org/resource/Keserwan_District', 'Kesernwan', inplace=True)
df.replace('http://dbpedia.org/resource/Marjeyoun_District', 'Marjeyoun', inplace=True)
df.replace('http://dbpedia.org/resource/Aley_District', 'Aley', inplace=True)
df.replace('https://dbpedia.org/page/Beqaa_Governorate', 'Beqaa', inplace=True)
df.replace('http://dbpedia.org/resource/Matn_District', 'Matn', inplace=True)
df.replace('http://dbpedia.org/resource/Miniyehâ\x80\x93Danniyeh_District', 'Miniyeh-Danniyeh', inplace=True)
df.replace('http://dbpedia.org/resource/Bint_Jbeil_District', 'Bint Jbeil', inplace=True)
df.replace('http://dbpedia.org/resource/Hasbaya_District', 'Hasbaya', inplace=True)
df.replace('http://dbpedia.org/resource/ZahlÃ©_District', 'Zahlé', inplace=True)
df.replace('http://dbpedia.org/resource/Western_Beqaa_District', 'Western Beqaa', inplace=True)
df.replace('https://dbpedia.org/page/Baalbek-Hermel_Governorate', 'Baalbek-Hermel', inplace=True)
df.replace('http://dbpedia.org/resource/Tripoli_District,_Lebanon', 'Tripoli', inplace=True)
df.replace('http://dbpedia.org/resource/Hermel_District', 'Hermel', inplace=True)


df.rename(columns={'refArea':'District'}, inplace=True)



st.title("Tourism Analysis in Lebanon - 2023")
st.markdown("Explore how tourism infrastructure is distributed across Lebanese towns and governorates.")

st.sidebar.header("Filters")

# district selector


districts = df['District'].unique()
selected_districts = st.sidebar.multiselect(
    "Select District:", options=districts, default=districts
)

# Variable selector
columns_map = {
    'Total number of hotels': 'Hotels',
    'Total number of cafes': 'Cafes',
    'Total number of guest houses': 'Guest Houses',
    'Total number of restaurants': 'Restaurants'
}
selected_variable = st.sidebar.selectbox(
    "Select a tourism facility to display:",
    options=list(columns_map.keys())
)

# Filter the dataset
filtered_df = df[df['District'].isin(selected_districts)]

# Bar Chart: Establishments per town
st.subheader(f"{columns_map[selected_variable]} by Town")
fig_bar = px.bar(
    filtered_df,
    y='Town',
    x=selected_variable,
    color='District',
    labels={'Town': 'Town', selected_variable: columns_map[selected_variable]},
    title=f"{columns_map[selected_variable]} per Town",
)
st.plotly_chart(fig_bar, use_container_width=True)

# Scatter Plot: Tourism Index vs Total Establishments
st.subheader("Tourism Index vs. Total Establishments")
filtered_df['Total Establishments'] = (
    filtered_df['Total number of hotels'] +
    filtered_df['Total number of cafes'] +
    filtered_df['Total number of guest houses'] +
    filtered_df['Total number of restaurants']
)

fig_scatter = px.scatter(
    filtered_df,
    x='Total Establishments',
    y='Tourism Index',
    color='District',
    hover_data=['Town'],
    title="Tourism Index vs. Total Number of Establishments"
)
st.plotly_chart(fig_scatter, use_container_width=True)

