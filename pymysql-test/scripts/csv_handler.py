import pandas as pd

class CsvFile:
    # def __init__(self, fileName):
    
    def read_csv(self, filePath):
        print("Hello World")
        
        df = pd.read_csv(filePath, encoding = "ISO-8859-1")
        print(df)

