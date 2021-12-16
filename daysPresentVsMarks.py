import plotly.express as px
import csv
import numpy as np

def plotFigure():
    with open("daysPresentVsMarks.csv") as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x ="Marks In Percentage", y = "Days Present")
        fig.show()

def getDataSource(data_path):
    marks = []
    daysPresent = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))
    
    return{"x": marks, "y": daysPresent}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("The correlation between the marks and the days present -- \n -> ", correlation[0,1])

def setup():
    data_path = "daysPresentVsMarks.csv"
    plotFigure()
    data_source = getDataSource(data_path)
    find_correlation(data_source)

setup()