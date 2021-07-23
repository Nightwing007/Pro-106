import csv
import numpy as np

def getDatasource(dataPath):
  array_1 = []
  array_2 = []
  value_1 = input("name of column 1: ")
  value_2 = input("name of column 2: ")
  with open (dataPath) as csvf :
   df = csv.DictReader(csvf)
   for row in df :
    array_1.append(float(row[value_1]))
    array_2.append(float(row[value_2]))
  return {"x" : array_2,"y" : array_1 }

def findCorrelation(dataSource):
  correlation = np.corrcoef(dataSource["x"],dataSource["y"])
  print("correlation is " , correlation[0,1])

def main():
  dataPath = input("Enter Data Source : ")
  dataSource = getDatasource(dataPath)
  findCorrelation(dataSource)

main()