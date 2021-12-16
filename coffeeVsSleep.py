import plotly.express as px
import csv
import numpy as np

def plotfigure():
    with open("coffeeVsSleep.csv") as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
        fig.show()

def getDataSource(data_path):
    coffee = []
    sleep = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    
    return{"x": coffee, "y": sleep}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("The correlation between the amount of coffee in ml and the hours of sleep -- \n -> ", correlation[0, 1])

def setup():
    data_path = "coffeeVsSleep.csv"
    plotfigure()
    data_source= getDataSource(data_path)
    find_correlation(data_source)

setup()