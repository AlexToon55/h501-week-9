''' Utility functions for data processing and model estimation.'''

import pandas as pd
import numpy as np


# Dummy class for group-level estimation
class GroupEstimate:
    def __init__(self, estimate="mean"):
        ''' Initialize the GroupEstimate model.'''
        if not estimate in ["mean", "median"]:
            raise ValueError("Estimate must be 'mean' or 'median'")
        
        self.estimate = estimate

        self.lookup_ = None
        self.columns_ = None
    
    def fit(self, X, y):
        ''' Fit the GroupEstimate model.'''

        # Store column names
        self.columns_ = list(X.columns)

        # Create a copy of X to avoid modifying the original data
        df = X.copy()
        df["_y"] = pd.Series(y).values

        # group-level estimates
        if self.estimate == "mean":
            self.lookup_ = df.groupby(self.columns_)["_y"].mean()
        else:
            self.lookup_ = df.groupby(self.columns_)["_y"].median()

        return self

    def predict(self, X):
        ''' Predict using the group-level estimates.'''

        # Create a copy of X to avoid modifying the original data
        df = X.copy()
        
        # Merge with lookup table to get predictions
        lok = self.lookup_.reset_index().rename(columns={"_y": "y_pred"})
    
        # Perform left join to get predictions
        df = df.merge(lok, on=self.columns_, how="left")

        # Extract predictions
        y_pred = df["y_pred"].values


        return y_pred