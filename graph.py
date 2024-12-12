import pandas as pd
import plotly.express as px
#import plotly.figure_factory as ff
import csv

df = pd.read_csv("Average Distance of Sports.csv")

value = df["Distance(Km)"].tolist()
count = ["Sports"].tolist()

fig = pd.DataFrame(df, x = "Distance(Km)", y = "Sports", show_hist = False)
print ("Create DataFrame:\n", df)

fig.show()

