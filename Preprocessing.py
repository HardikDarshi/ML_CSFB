import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
class Preprocessor:
    """
        This class shall  be used to clean and transform the data before training.
        Written By:Hardik Patel
        """
    def remove_columns(self,data,columns):
        """
                Method Name: remove_columns
                Description: This method removes the given columns from a pandas dataframe.
                Output: A pandas DataFrame after removing the specified columns.
        """
        self.data=data
        self.columns=columns
        try:
            self.useful_data=self.data.drop(self.columns, axis=1) # drop the labels specified in the columns
            print('Column removal Successful.Exited the remove_columns method of the Preprocessor class')
            return self.useful_data
        except Exception as e:
            return print('Error %s' % e)
            raise Exception()

    def handle_missing_values(self, data):
        """
                                        Method Name: impute_missing_values
                                        Description: This method replaces all the missing values in the Dataframe using KNN Imputer.
                                        Output: A Dataframe which has all the missing values imputed.
        """
        self.data = data
        try:
            self.data.fillna(0, inplace=True)
            print('Missing values replace with 0 in all columns')
            return self.data
        except Exception as e:
            print('Exception message of handle_missing_values:  ' + str(e))
            raise Exception()

    def handle_categorical(self, data):
        self.data = data
        try:
            cleanup = {'OK': 1, 'Error': 0}
            self.data.replace(cleanup, inplace=True)
            return self.data
            print('categorical data is handling done')
        except Exception as e:
            print('Exception message % s' % e)
            raise Exception()

    def int_to_categorical(self, data):
        self.data = data
        try:
            cleanup1 = {1 : 'OK', 0 : 'Error'}
            self.data.replace(cleanup1, inplace = True)
            print('prediction is converted to categorical data')
            return self.data
        except Exception as e:
            print('Exception message % s' % e)
            raise Exception()

