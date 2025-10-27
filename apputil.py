''' Utility functions for data processing and model estimation.'''

import pandas as pd
import numpy as np


# Dummy class for group-level estimation
class GroupEstimate:
    def __init__(self, estimate="mean"):
        if not estimate in ["mean", "median"]:
            raise ValueError("Estimate must be 'mean' or 'median'")
        
        self.estimate = estimate

        self.lookup_ = None
        self.columns_ = None
    
    def fit(self, X, y):

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
        raise NotImplementedError("Not Implemented")