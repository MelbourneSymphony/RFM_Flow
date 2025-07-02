import streamlit as st
import pandas as pd
import plotly.graph_objects as go


st.set_page_config(layout="centered")
st.title("MSO RFM Segmentation Flows")

df= pd.read_csv('https://raw.githubusercontent.com/MelbourneSymphony/RFM_Flow/refs/heads/main/2025_july_major_sankey.csv')
unique_source_target = list(pd.unique(df[['Source', 'Target']].values.ravel('K')))
mapping_dict = {k: v for v, k in enumerate(unique_source_target)}
df['Source'] = df['Source'].map(mapping_dict)
df['Target'] = df['Target'].map(mapping_dict)
links_dict = df.to_dict(orient='list')
color_dict = ['#f94144',  # New Customer
 '#f94144',  # New Customer q4
 '#749a7f',  # Not Previously purchased
 '#749a7f',  # Not previously purchased q4
 '#577590',  # Slipping
 '#577590',  # Slipping q4
 '#277da1',  # Lost Touch
 '#277da1',  # Lost Touch q4
 '#749a7f',  # Not previously purchased q1
 '#277da1',  # Lost Touch q1
 '#f94144',  # New Customer q1
 '#577590',  # Slipping q1
 '#749a7f',  # Not previously purchased q2
 '#277da1',  # Lost Touch q2
 '#f94144',  # New Customer q2
 '#577590',  # Slipping q2 
 '#749a7f',  # not previously purchased q3
 '#277da1',  # Lost Touch q3
 '#f94144',  # New customer q3
 '#577590',  # Slipping q3 
 '#819096',  # Dropped Outside Timeframe
 '#819096',  # Dropped Outside Timeframe q1
 '#819096',  # Drop off
 '#819096',  # Drop off q3 
 '#f94144',  # New customer q5 
 '#819096',  # Dropped Outside Timeframe  q3
 '#277da1',  # Lost touch q5 
 '#577590'  # Slipping q5             
]

color_dict_link = df['link_colour'].tolist()



#First Sankey
fig = go.Figure(data=[go.Sankey(
    node = dict(
     align='center',
      pad = 20,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = unique_source_target,
      color = color_dict,
    ),
    link = dict(
      arrowlen = 15,
      source = links_dict["Source"],
      target = links_dict["Target"],
      value = links_dict["values"],
      color = color_dict_link,

  ))])

fig.update_layout(title_text="RFM Customer Flow", font_size=10,width=1000, height=600,

  xaxis={
  'showgrid': False, # thin lines in the background
  'zeroline': False, # thick line at x=0
  'visible': False,  # numbers below
  },
  yaxis={
  'showgrid': False, # thin lines in the background
  'zeroline': False, # thick line at x=0
  'visible': False,  # numbers below
  }, plot_bgcolor='rgba(0,0,0,0)')

for x_coordinate, column_name in enumerate(["Aug 2023","Nov 2023","April 2024","July 2024","Nov 2024","July 2025"]):
    fig.add_annotation(
          x=x_coordinate,#Plotly recognizes 0-5 to be the x range.

          y=1.075,#y value above 1 means above all nodes
          xref="x",
          yref="paper",
          text=column_name,#Text
          showarrow=False,
          font=dict(
              family="Tahoma",
              size=12,
              color="black"
              ),
          align="left",
          )
st.plotly_chart(fig, use_container_width=True)
#sankey 2
df2= pd.read_csv('https://raw.githubusercontent.com/MelbourneSymphony/RFM_Flow/refs/heads/main/2025_july_minor_sankey.csv')
unique_source_target2 = list(pd.unique(df2[['Source', 'Target']].values.ravel('K')))
mapping_dict = {k: v for v, k in enumerate(unique_source_target2)}
df2['Source'] = df2['Source'].map(mapping_dict)
df2['Target'] = df2['Target'].map(mapping_dict)
links_dict2 = df2.to_dict(orient='list')

colours2 = [
 '#58b0d6',  # Top Tier
 '#58b0d6',  # Top Tier q4
 '#f9c74f',  # Affluent
 '#f9c74f',  # Affluent q4
 '#f3722c',  # Faithful
 '#f3722c',  # Faithful q4
 '#90be6d',  # Loyal Purchaser
 '#90be6d',  # Loyal Purchaser q4
 '#f9c74f',  # Affluent q1
 '#f3722c',  # Faithful q1
 '#90be6d',  # Loyal Purchaser q1
 '#58b0d6',  # Top Tier q1
 '#f9c74f',  # Affluent q2
 '#f3722c',  # Faithful q2
 '#90be6d',  # Loyal Purchaser q2
 '#58b0d6',  # Top Tier q2
 '#f9c74f',  # Affluent q3
 '#f3722c',  # Faithful q3
 '#58b0d6',  # Top Tier q3
 '#577590',  # Slipping q4
 '#577590',  # Slipping q1
 '#577590',  # Slipping q2
 '#58b0d6',  # Top Tier q5
 '#577590',  # Slipping q5
 '#f3722c',  # Faithful q5
 '#f9c74f'  # Affluent q5
]
link_colours_minor = df2['link_colour'].to_list()

#Sankey Diagram Code
fig2 = go.Figure(data=[go.Sankey(
    node = dict(
     align='center',
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = unique_source_target2,
      color = colours2,
    ),
    link = dict(
      arrowlen = 15,
      source = links_dict2["Source"],
      target = links_dict2["Target"],
      value = links_dict2["values"],
      color = link_colours_minor,

  ))])

fig2.update_layout(title_text="RFM Customer Minor Flow", font_size=10,width=1000, height=600,

  xaxis={
  'showgrid': False, # thin lines in the background
  'zeroline': False, # thick line at x=0
  'visible': False,  # numbers below
  },
  yaxis={
  'showgrid': False, # thin lines in the background
  'zeroline': False, # thick line at x=0
  'visible': False,  # numbers below
  }, plot_bgcolor='rgba(0,0,0,0)')

for x_coordinate, column_name in enumerate(["Aug 2023","Nov 2023","April 2024","July 2024","Nov 2024","July 2025"]):
    fig2.add_annotation(
          x=x_coordinate,#Plotly recognizes 0-5 to be the x range.

          y=1.075,#y value above 1 means above all nodes
          xref="x",
          yref="paper",
          text=column_name,#Text
          showarrow=False,
          font=dict(
              family="Tahoma",
              size=12,
              color="black"
              ),
          align="left",
          )
st.plotly_chart(fig2, use_container_width=True)

st.write("to go back to the main dashboard click [here](https://mso-rfmscatter.streamlit.app/)")
