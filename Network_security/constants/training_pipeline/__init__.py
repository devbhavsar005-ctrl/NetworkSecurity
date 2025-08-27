import os 
import sys 
import numpy as np 
import pandas as pd 

"""
   defining  common constant for training pipeline
"""

TARGET_COLUMN= "result"
PIPELINE_NAME:str="Network_security"
ARTIFACT_DIR:str="artifacts"
FILE_NAME:str="phisingData.csv"

TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"

"""
    this are the constants which is use full for data ingestion process
"""
DATA_INGESTION_COLLECTION_NAME:str="NetworksecurityData"
DATA_INGESTION_DATABASE_NAME:str="Dev_database"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FETAURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.20
