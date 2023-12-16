import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("Student Marks vs Days Present.csv")

print(df.groupby("Marks In Percentage")["Days Present"].mean())

fig = go.Figure(go.Bar(
                x=("Roll No"),
                y=("Marks In Percentage"),
                orientation='h'))
fig.show()