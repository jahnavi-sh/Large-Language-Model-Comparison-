#Import libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

#Download dataset into pandas dataframe 
data=pd.read_csv('LLMs.csv')

#view the dataset 
data.head()

data['date']=data['date'].apply(lambda x: datetime.strptime(x.replace('July','Jul'), "%b %Y"))
data=data.sort_values('date',ascending=False).reset_index(drop=True)
display(data)

owners=sorted(data['owner'].unique().tolist())
print(owners)

for ow in owners:
    datai=data[data['owner']==ow]
    fig = px.bar(datai, x='name', y='trained on x billion parameters',title=ow)
    fig.show()