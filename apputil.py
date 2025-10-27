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
        raise NotImplementedError("Not Implemented")

    def predict(self, X):
        raise NotImplementedError("Not Implemented")