import numpy as np
import pandas as pd
import re

def readFile(): 

    read_file = "/home/paul/Programming/Python/MyMiniProjects/Mid/Strong/strong.xlsx"
    out_file = "/home/paul/Programming/Python/MyMiniProjects/Mid/Strong/output.csv"
    
    data = pd.read_excel(read_file)
    num = data.to_numpy()
    dataArray = []

    for line in num: 
        parsedData = line[0].split(";")
        for index, element in enumerate(parsedData):
            final = element.replace('"', '')
            parsedData[index] = final
        dataArray.append(parsedData)

    
    df = pd.DataFrame(dataArray, columns = ["Date", "Workout Name", "Exercise Name", "Set Order", "Weight", "Weight Unit", "Reps", "RPE", "Distance", "Distance Unit", "Seconds", "Notes", "Workout Notes", "Workout Duration"])
       

    df.to_csv(out_file, sep='\t', encoding='utf-8')

readFile()

