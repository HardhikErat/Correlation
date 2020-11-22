import plotly.express as px
import csv

with open("IC vs T.csv", newline='') as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Temperature", y="Ice Sales")
    fig.show()