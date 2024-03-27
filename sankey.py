import streamlit as st
import pandas as pd
import plotly.graph_objects as go


st.set_page_config(layout="centered")
st.set_option('deprecation.showPyplotGlobalUse', True)
st.title("MSO RFM Segmentation Flows")

df= pd.read_csv('/content/rfm sankey.csv')
unique_source_target = list(pd.unique(df[['Source', 'Target']].values.ravel('K')))
mapping_dict = {k: v for v, k in enumerate(unique_source_target)}
df['Source'] = df['Source'].map(mapping_dict)
df['Target'] = df['Target'].map(mapping_dict)
links_dict = df.to_dict(orient='list')
color_dict = ['rgba(252,65,94,0.7)', 'rgba(255,162,0,0.7)','rgba(55,178,255,0.7)','rgba(66, 95, 252, 0.89)',
 'rgba(43, 215, 116, 0.7)','rgba(243, 93, 6, 0.7)','rgba(0, 36, 165, 0.86)','rgba(141, 53, 131, 0.96)',
 'rgba(252,65,94,0.7)','rgba(255,162,0,0.7)', 'rgba(55,178,255,0.7)', 'rgba(66, 95, 252, 0.89)',
 'rgba(43, 215, 116, 0.7)', 'rgba(243, 93, 6, 0.7)', 'rgba(141, 53, 131, 0.96)','rgba(0, 36, 165, 0.86)']
 color_dict_link = ['rgba(252,65,94,0.4)', 'rgba(255,162,0,0.4)', 'rgba(55,178,255,0.4)', 'rgba(255,162,0,0.4)', 'rgba(252,65,94,0.4)', 'rgba(66, 95, 252, 0.4)', 'rgba(55,178,255,0.4)', 'rgba(43, 215, 116, 0.4)', 'rgba(66, 95, 252, 0.4)', 'rgba(243, 93, 6, 0.4)', 'rgba(0, 36, 165, 0.4)', 'rgba(66, 95, 252, 0.4)', 'rgba(43, 215, 116, 0.4)', 'rgba(255,162,0,0.4)', 'rgba(243, 93, 6, 0.4)', 'rgba(0, 36, 165, 0.4)', 'rgba(141, 53, 131, 0.4)', 'rgba(243, 93, 6, 0.4)', 'rgba(141, 53, 131, 0.4)', 'rgba(0, 36, 165, 0.4)', 'rgba(141, 53, 131, 0.4)', 'rgba(252,65,94,0.4)', 'rgba(252,65,94,0.4)', 'rgba(43, 215, 116, 0.4)', 'rgba(66, 95, 252, 0.4)', 'rgba(243, 93, 6, 0.4)', 'rgba(0, 36, 165, 0.4)', 'rgba(141, 53, 131, 0.4)', 'rgba(255,162,0,0.4)', 'rgba(55,178,255,0.4)', 'rgba(43, 215, 116, 0.4)', 'rgba(0, 36, 165, 0.4)', 'rgba(141, 53, 131, 0.4)', 'rgba(243, 93, 6, 0.4)', 'rgba(255,162,0,0.4)', 'rgba(141, 53, 131, 0.4)']

#First Sankey
fig = go.Figure(data=[go.Sankey(
    node = dict(
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

for x_coordinate, column_name in enumerate(["2023 Quarter 3","2023 Quarter 4"]):
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
fig.show()
#sankey 2
df2= pd.read_csv('/content/sankey_minor_flow.csv')
unique_source_target2 = list(pd.unique(df2[['Source', 'Target']].values.ravel('K')))
mapping_dict = {k: v for v, k in enumerate(unique_source_target2)}
df2['Source'] = df2['Source'].map(mapping_dict)
df2['Target'] = df2['Target'].map(mapping_dict)
links_dict2 = df2.to_dict(orient='list')

colours2 =['rgba(255,162,0,0.7)','rgba(66, 95, 252, 0.89)','rgba(55,178,255,0.7)','rgba(43, 215, 116, 0.7)',
           'rgba(0, 36, 165, 0.86)','rgba(252,65,94,0.7)','rgba(43, 215, 116, 0.7)','rgba(55,178,255,0.7)',
           'rgba(255,162,0,0.7)','rgba(66, 95, 252, 0.89)']
rgba_codes = [
    'rgba(255,162,0,0.4)',   # 0 Loyal Purch
     'rgba(255,162,0,0.4)',   # 0 Loyal Purch
    'rgba(66, 95, 252, 0.4)',  # Faithful
    'rgba(55,178,255,0.4)',  # Top Tier
    'rgba(43, 215, 116, 0.4)',  # Affluent
    'rgba(66, 95, 252, 0.4)',  # Faithful
    'rgba(0, 36, 165, 0.4)',  # not prev purch
    'rgba(66, 95, 252, 0.4)',  # Faithful
    'rgba(43, 215, 116, 0.4)',  # Affluent
    'rgba(255,162,0,0.4)',   # 0 Loyal Purch
    'rgba(0, 36, 165, 0.4)',  # not prev purch
    'rgba(0, 36, 165, 0.4)',  # not prev purch
    'rgba(43, 215, 116, 0.4)',  # Affluent
    'rgba(66, 95, 252, 0.4)',  # Faithful
    'rgba(255,162,0,0.4)',   # 0 Loyal Purch
    'rgba(43, 215, 116, 0.4)',  # Affluent
    'rgba(0, 36, 165, 0.4)',  # not prev purch
    'rgba(255,162,0,0.4)',   # 0 Loyal Purch
]
#Sankey Diagram Code
fig = go.Figure(data=[go.Sankey(
    node = dict(
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
      color = rgba_codes,

  ))])

fig.update_layout(title_text="RFM Customer Minor Flow", font_size=10,width=1000, height=600,

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

for x_coordinate, column_name in enumerate(["2023 Quarter 3","2023 Quarter 4"]):
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
fig.show()
