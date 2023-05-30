import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge,  Lasso, ElasticNet
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from src.exception import CustomeException
from src.logger import logging

from src.utills import save_object,evaluate_model
from dataclasses import dataclass
import sys,os 

@dataclass
class ModelTrainerconfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerconfig()

    def initiate_model_training(self,train_arr,test_arr):
        try:
            logging.info('Splittingb dependent and independent feature from train and test data')
            X_train,y_train,X_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            models={
                'LinearRegression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'Elasticnet':ElasticNet(),
                'DecisionTree':DecisionTreeRegressor(),
                'RandomForest':RandomForestRegressor()
            }

            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print('='*30)
            logging.info(f'Model Report : {model_report}')
            # To get best score
            best_model_score = max(sorted(model_report.values()))
            # To get best model name
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            print(f'Best model found, Model name: {best_model_name}, R2 score: {best_model_score}')
            print('='*30)
            logging.info(f'Best model found, Model name: {best_model_name}, R2 score: {best_model_score}')
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
        except Exception as e:
            raise CustomeException(e,sys)
