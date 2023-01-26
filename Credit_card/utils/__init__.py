import pandas as pd
import os,sys
from Credit_card.config import mongo_client
from Credit_card.exception import Credit_cardException
from Credit_card.logger import logging

def get_collection_as_dataframe(database_name=str,collection_name=str)->pd.DataFrame:
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        if"id" in df.columns:
            logging.info(f"Droping columns:_id")
            df=df.columns("id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise Credit_cardException(e,sys)   

