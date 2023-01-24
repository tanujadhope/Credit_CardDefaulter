import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.

client = pymongo.MongoClient("mongodb+srv://TanujaDhope1:admin78@cluster0.aojtki0.mongodb.net/?retryWrites=true&w=majority")

DATABASE_NAME="bank_credits"
COLLECTION_NAME="creadit_card"
DATA_FILE_PATH="E:\VScode\CreditCarddefaulter\default-of-credit-card-clients.csv"

if __name__=="__main__":
 df=pd.read_csv(DATA_FILE_PATH)
 print(f"ROWS and COLUMNS :{df.shape}")
 

 ##Convert dataframe in json format so that we can dump dataset in mongodb ,reset index
 df.reset_index(drop=True,inplace=True)
 json_record=list(json.loads(df.T.to_json()).values()) ## convert in json fromat,interchange rows and columns and load 
   ### rows to column ,convert into list 
 print(json_record[1])  
 # insert coverted json record to mongodb 
 client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
