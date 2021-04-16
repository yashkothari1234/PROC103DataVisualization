import pandas as pd

import plotly.express as px

#reading data from csv files
df = pd.read_csv("CovidData.csv")
fig = px.scatter(df, x="date", y="cases",color="country")
fig.show()