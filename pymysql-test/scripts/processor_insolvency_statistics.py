import pandas as pd
import math
import os

class parser:

    def province_fill(self, csv_path: str):
        # Method 1
        # Populate Column 1 with corresponding province name.
        # iterate for each row the province name to fill up wherever there is NaN
        
        province_name = ''
        csv_data = pd.read_csv(csv_path, header = None, encoding = "ISO-8859-1")

        for index, row in enumerate(csv_data.iloc[:,0]):
            if pd.notna(row):
                province_name = row
            else:
                csv_data.iat[index,0]=province_name

        print(csv_data)
        # csv_path.replace(".csv", "_cleaned.csv")
        csv_path = os.path.splitext(csv_path)[0]
        csv_path = csv_path+'_cleaned.csv'
        print(csv_path)
        csv_data.to_csv(csv_path, header = None, index = None)
                
                
        