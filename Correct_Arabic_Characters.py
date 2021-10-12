import pandas as pd
import os
import random
import sys
import glob
import os.path

def enc(dataframe_path):
    df = pd.read_csv(dataframe_path,sep="\t",encoding="cp1256")
    path = "cleaned\\"
    df.to_excel(path+"output{}.xlsx".format(random.randint(0,999999)))


      
if __name__ == "__main__":
    
    try:
        while True:
            dirname = os.path.dirname(__file__)

            folder_path = dirname+ '\downloaded\\'
            print("Loading ...")
            file_type = '\*tsv'
            files = glob.glob(folder_path + file_type)
            max_file = max(files, key=os.path.getctime)
            print(max_file)
            
            #print(max_file)
            enc(max_file)
            
            dirname = os.path.dirname(__file__)
            folder_path = dirname+ '\cleaned\\'
            #print(folder_path)
            file_type = '\*xlsx'
            files = glob.glob(folder_path + file_type)
            max_file = max(files, key=os.path.getctime)
            print(max_file)
            os.startfile(max_file)
            input("successfully done")
    except Exception as e:
        print(e)
        input('Enter to close')