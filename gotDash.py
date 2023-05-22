#!/usr/bin/env python
# coding: utf-8

# In[6]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Create the app
app = dash.Dash(__name__)



#sentiment = pd.read_csv('C:\\dash\\GoT Sentiment.csv')
#fig = px.histogram(sentiment, x='date', y=['positive','negative','neutral'], 
#                   title = "This is title",barmode='group'
#                   labels={
#                     "sepal_length": "Sepal Length (cm)",
#                     "sepal_width": "Sepal Width (cm)",
#                     "variable": "Species of Iris"
#                 },                 
#                  )

sentiment = pd.read_csv('C:\\dash\\GoT Sentiment.csv')

fig = px.histogram(sentiment, x='date', nbins=20, y=['positive','negative','neutral'], 
                    title = "GoT Sentiment per Month",barmode='group',
                    labels={
                     "date": "Month",
                     "variable": "Sentiment"
                 },                
                )

fig.update_layout(font=dict(family="Courier New, monospace",size=14,color="RebeccaPurple"), yaxis_title= "Sentiment")

app.layout = html.Div(children=[
    html.H1(
        children='Game of Thrones Sentiment',
        style={
            'fontFamily': 'Courier New, monospace', 
            'fontSize': '24px'  
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

#app.layout = html.Div(children=[
#   html.H1(children='Hello Dash'),  # Create a title with H1 tag


#   dcc.Graph(
#       id='example-graph',
#       figure=fig
#   )  # Display the Plotly figure
#])




if __name__ == '__main__':
   app.run_server(debug=True) # Run the Dash app


# In[ ]:




