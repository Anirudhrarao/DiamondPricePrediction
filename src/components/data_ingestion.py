import os
import sys
from src.logger import logging
from src.exception import CustomeException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Initialize the data ingestion configuaration

@dataclass #(here we do not include __init__ method for creating vars)
class DataIngestionconfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','raw.csv')

# Create the data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()   
    
    def initiate_data_ingestion(self):
        logging.info('Data method ingestion method starts')
        try:
            df = pd.read_csv(os.path.join('notebooks/data/gemstone.csv'))
            logging.info('Dataset read as pandas dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Raw data is created successfully')

            train_set,test_set = train_test_split(df,test_size=0.3,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('Ingestion of data is completed')
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info('Exception occured at data ingestion stage')
            raise CustomeException(e,sys)
        